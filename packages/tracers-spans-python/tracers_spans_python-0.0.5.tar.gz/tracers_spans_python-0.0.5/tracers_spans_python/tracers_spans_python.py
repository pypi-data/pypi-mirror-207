from functools import wraps
import aiozipkin as az

class Tracer:
    def __init__(
            self,
            host = f'localhost',
            port = '9411/api/v2/spans',
            service_name = 'Tracer',
            ip_application="0.0.0.0",
            port_detail=8000
            ):
        
        # Setup zipkin conections/configurations.
        self.host = host
        self.port = port
        self.service_name = service_name
        self.ipv4 = ip_application
        self.port_detail = port_detail
        
        # Here is a conection with zipkin and yours settings.
        self.zipkin_address = f"http://{self.host}:{self.port}"
        # Here is features of endpoint.
        self.endpoint = az.create_endpoint(self.service_name, ipv4='0.0.0.0', port=self.port_detail)

    # Frunction to setup the tracer
    async def create_tracer(self):
        res = await az.create(self.zipkin_address, self.endpoint, sample_rate=1.0)
        return res
    
    # This function is to add annotate in a trace
    def annotate_tracer(self, annotate : str = None,):
        span = self.span
        return span.annotate(annotate)
    
    # This function is to add annotate in a span
    def annotate_span(self, annotate : str = None,):
        span = self.nested_span
        return span.annotate(annotate)
    
    # This function is to add tags in a tracer
    def tags_tracer(self, key : str = None, value: str = None):
        span = self.span
        return span.tag(key, value)
    
    # This function is to add tags in a child span
    def tags_child(self, key : str = None, value: str = None):
        span = self.nested_span
        return span.tag(key, value)
    
    async def test_async ():
        pass

    # Use to create a new tracer, in endpoints for examples.
    def new_tracer(self):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                tool = Tracer(
                    host=self.host, ip_application=self.ipv4,
                    port=self.port,
                    service_name=self.service_name
                )
                self.tracer = await tool.create_tracer()
                with self.tracer.new_trace(sampled=True) as self.span:
                    self.span.name(func.__name__)
                    
                    result = func(*args, **kwargs)


                return result
            return wrapper
        return decorator
    
    def new_async_tracer(self):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                tool = Tracer(
                    host=self.host, ip_application=self.ipv4,
                    port=self.port,
                    service_name=self.service_name
                )
                self.tracer = await tool.create_tracer()
                with self.tracer.new_trace(sampled=True) as self.span:
                    self.span.name(func.__name__)
                    
                    result = await func(*args, **kwargs)


                return result
            return wrapper
        return decorator

    # Use in functions to create a childs in a main tracer.
    def new_child(self):
        def decorator(func):
            try:
                @wraps(func)
                def wrapper(*args, **kwargs):
                    span = self.span
                    with self.tracer.new_child(span.context) as self.nested_span:
                        self.nested_span.name(func.__name__)
                        
                        result = func(*args, **kwargs)

                    return result
                return wrapper
            except:
                @wraps(func)
                async def wrapper(*args, **kwargs):
                    span = self.span
                    with self.tracer.new_child(span.context) as self.nested_span:
                        self.nested_span.name(func.__name__)
                        
                        result = await func(*args, **kwargs)

                    return result
                return wrapper
        return decorator
    
    def new_async_child(self):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                span = self.span
                with self.tracer.new_child(span.context) as self.nested_span:
                    self.nested_span.name(func.__name__)
                    result = await func(*args, **kwargs)

                return result
            return wrapper
        return decorator