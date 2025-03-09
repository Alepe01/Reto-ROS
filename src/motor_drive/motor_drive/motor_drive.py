import rclpy
import serial
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class MotorDrive(Node):
    def __init__(self):
        super().__init__('motor_drive')
        self.subscription = self.create_subscription(Float64MultiArray, '/angulos_calculados', self.recibir_angulos, 10)
        self.get_logger().info('Nodo motor_drive iniciado')

        # Configuración del puerto serial (ajusta el puerto según corresponda)
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Cambia '/dev/ttyUSB0' según el puerto de la ESP32
            self.get_logger().info('Conexión serial establecida con ESP32')
        except serial.SerialException as e:
            self.get_logger().error(f'Error al abrir el puerto serial: {e}')
            self.ser = None

    def recibir_angulos(self, msg):
        self.get_logger().info(f'Recibidos ángulos para motores: {msg.data}')
        
        if self.ser:
            try:
                # Convertir los valores en una cadena con el formato esperado por la ESP32
                angulo_str = f"{int(msg.data[0])},{int(msg.data[1])}\n"
                self.ser.write(angulo_str.encode())  # Enviar datos a ESP32
                self.get_logger().info(f'Enviado a ESP32: {angulo_str}')
            except Exception as e:
                self.get_logger().error(f'Error al enviar datos: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = MotorDrive()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
