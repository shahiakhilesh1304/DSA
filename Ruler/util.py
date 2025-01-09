from Ruler.Analyzer import ComplexityAnalyzer
import inspect


def start(func_name):
    analyzer = ComplexityAnalyzer()
    source = inspect.getsource(func_name)
    return analyzer,source

def report(analyzer,source,func_name):
    source = inspect.getsource(func_name)
    result = analyzer.analyze_source(source)
    print(f"\n\n\n\nComplexity Report \n\nFunction: {result['name']}")
    print(f"Complexity: {result['complexity']}")