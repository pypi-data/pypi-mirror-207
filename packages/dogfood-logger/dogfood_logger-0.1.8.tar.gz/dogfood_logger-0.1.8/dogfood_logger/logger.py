import logging_loki
from dotenv import load_dotenv
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry import trace
import logging
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.exporter.jaeger.thrift import \
    JaegerExporter as ThriftJaegerExporter

class LokiLogger:

    def __init__(self, app, app_name, url, log_format, env, agent_host, agent_port) -> None:
        self.handler = logging_loki.LokiHandler(
            url=url,
            tags={"application": app_name},
            version="1",
        )
        self.handler.setFormatter(logging.Formatter(log_format))
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig()
        self.logger.addHandler(self.handler)
        self.resource = Resource.create(attributes={
            "service.name": app_name, # for Tempo to distinguish source
            "compose_service": app_name # as a query criteria for Trace to logs
        })
        self.tracer = TracerProvider(resource=self.resource)
        trace.set_tracer_provider(self.tracer)
        self.tracer.add_span_processor(BatchSpanProcessor(ThriftJaegerExporter(
            agent_host_name=agent_host,
            agent_port=agent_port,
        )))
        self.env = env
        LoggingInstrumentor().instrument()
        FastAPIInstrumentor.instrument_app(app, tracer_provider=self.tracer)

    def log_loki(self, msg, level):
        self.logger.debug(
            msg,
            extra={"tags": {"env": self.env, "level": level}},
        )

    def error(self, msg):
        self.logger.error(
            msg,
            extra={"tags": {"env": self.env, "level": "error"}},
        )

    def debug(self, msg):
        self.logger.debug(
            msg,
            extra={"tags": {"env": self.env, "level": "debug"}},
        )

    def critical(self, msg):
        self.logger.critical(
            msg,
            extra={"tags": {"env": self.env, "level": "critical"}},
        )

    def warn(self, msg):
        self.logger.warning(
            msg,
            extra={"tags": {"env": self.env, "level": "warn"}},
        )

    def info(self, msg):
        self.logger.info(
            msg,
            extra={"tags": {"env": self.env, "level": "info"}}
        )

    def exception(self, msg):
        self.logger.exception(
            msg,
            extra={"tags": {"env": self.env, "level": "exception"}},
        )

