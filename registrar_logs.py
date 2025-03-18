from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configurar o provedor de traces
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))

tracer = trace.get_tracer(__name__)

def registrar_logs(nome_algoritmo, tamanho_dados, tempo_execucao, comparacoes, trocas):
    with tracer.start_as_current_span("executar_algoritmo"):
        print(f"Algoritmo: {nome_algoritmo}")
        print(f"Tamanho dos dados: {tamanho_dados}")
        print(f"Tempo de execução: {tempo_execucao:.2f} ms")
        print(f"Comparações: {comparacoes}")
        print(f"Trocas: {trocas}")
        print("-" * 40)


jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))