import grpc
import generateimage_pb2
import generateimage_pb2_grpc
from concurrent import futures

class ImageGenerator(generateimage_pb2_grpc.GenerateImageServicer):
    def CanGenerate(self, request, context):
        # Response to server if it can generate the image
        canGenerate = True
        return generateimage_pb2.CanGenerateResponse(canGenerate=canGenerate)


def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generateimage_pb2_grpc.add_GenerateImageServicer_to_server(
        ImageGenerator(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    print('Server started at port {}'.format(port))
    server.wait_for_termination()

if __name__ == '__main__':
    serve()