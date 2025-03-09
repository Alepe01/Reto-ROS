import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class SolicitudServicio(Node):
    def __init__(self):
        super().__init__('solicitud_servicio')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/angulos_deseados', 10)
        self.get_logger().info('Nodo solicitud_servicio iniciado')

    def publicar_angulos(self, xd, yd):
        msg = Float64MultiArray()
        msg.data = [xd, yd]
        self.publisher_.publish(msg)
        self.get_logger().info(f'📡 Coordenadas enviadas: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SolicitudServicio()

    try:
        while True:
            try:
                entrada = input("Ingrese las coordenadas xd, yd (ejemplo: 50,30) o 'q' para salir: ")
                if entrada.lower() == 'q':
                    break
                
                xd, yd = map(float, entrada.split(','))
                node.publicar_angulos(xd, yd)
            except ValueError:
                print("❌ Entrada no válida. Use el formato correcto (ejemplo: 50,30).")
    except KeyboardInterrupt:
        print("\n🔴 Terminando nodo.")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
