from Ruler.Analyzer import ComplexityAnalyzer
import inspect


def start(function):
    analyzer = ComplexityAnalyzer()
    source = inspect.getsource(function)
    return analyzer,source

def report(analyzer,source,function):
    source = inspect.getsource(function)
    result = analyzer.analyze_source(source)
    print(f"\n\n\n\nComplexity Report \n\nFunction: {result['name']}")
    print(f"Complexity: {result['complexity']}")