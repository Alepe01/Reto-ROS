import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import math

class CinematicaInversa(Node):
    def __init__(self):
        super().__init__('cinematica_inversa')

        # Longitudes de los eslabones (en mm)
        self.L1 = 60.0
        self.L2 = 80.0

        # Suscriptor para recibir la posición deseada (xd, yd)
        self.subscription = self.create_subscription(
            Float64MultiArray,
            '/angulos_deseados',
            self.calcular_cinematica_inversa,
            10)
        
        # Publicador de los ángulos calculados
        self.publisher = self.create_publisher(
            Float64MultiArray,
            '/angulos_calculados',
            10)

        self.get_logger().info('Nodo cinematica_inversa iniciado')

    def calcular_cinematica_inversa(self, msg):
        xd, yd = msg.data  # Extraer posición deseada
        self.get_logger().info(f'Recibida posición deseada: {msg.data}')

        # Distancia desde la base hasta el efector final
        r = math.sqrt(xd**2 + yd**2)

        # Verificar si el punto está dentro del alcance
        if r > (self.L1 + self.L2) or r < abs(self.L1 - self.L2):
            self.get_logger().warn("⚠️ Posición fuera del alcance. No se puede calcular.")
            return

        # **Nueva fórmula para θ2**
        cos_theta2 = (xd**2 + yd**2 - (self.L1**2 + self.L2**2)) / (2 * self.L1 * self.L2)
        theta2 = math.acos(cos_theta2)

        # Ajustar la convención de θ2: negativo si está hacia la izquierda
        if xd < 0:
            theta2 = -theta2

        # Calcular θ1 con la nueva referencia
        alpha = math.atan2(yd, xd)  # Ángulo del vector (xd, yd)
        beta = math.acos((self.L1**2 + r**2 - self.L2**2) / (2 * self.L1 * r))
        theta1 = alpha + beta  # Se ajusta la referencia

        # Convertir a grados
        theta1 = math.degrees(theta1)
        theta2 = math.degrees(theta2)

        # **Límite de movimiento para θ1 entre 0° y 180°**
        if theta1 < 0:
            theta1 = 0.0
        elif theta1 > 180:
            theta1 = 180.0

        self.get_logger().info(f'Publicados ángulos corregidos: θ1 = {theta1}°, θ2 = {theta2}°')

        # Publicar los ángulos calculados
        msg_out = Float64MultiArray()
        msg_out.data = [theta1, theta2]
        self.publisher.publish(msg_out)

def main(args=None):
    rclpy.init(args=args)
    node = CinematicaInversa()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
