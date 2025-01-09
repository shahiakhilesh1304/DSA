import ast
import inspect
import types
import sys
from typing import Dict, Any, Optional

class ComplexityAnalyzer:
    def __init__(self):
        self.complexity_map = {
            'constant': 'O(1)',
            'linear': 'O(n)',
            'quadratic': 'O(n²)',
            'cubic': 'O(n³)',
            'logarithmic': 'O(log n)',
            'linearithmic': 'O(n log n)',
            'exponential': 'O(2ⁿ)'
        }
        
    def analyze_node(self, node: ast.AST) -> str:
        if isinstance(node, ast.For):
            nested_complexity = self.analyze_node_list(node.body)
            if 'n²' in nested_complexity:
                return 'O(n³)'
            elif 'n' in nested_complexity:
                return 'O(n²)'
            return 'O(n)'
            
        elif isinstance(node, ast.While):
            nested_complexity = self.analyze_node_list(node.body)
            if 'n' in nested_complexity:
                return 'O(n²)'
            return 'O(n)'
            
        elif isinstance(node, (ast.If, ast.IfExp)):
            return 'O(1)'
            
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in ['sorted', 'sort']:
                    return 'O(n log n)'
                elif node.func.id in ['min', 'max', 'sum']:
                    return 'O(n)'
            return 'O(1)'
            
        return 'O(1)'

    def analyze_node_list(self, nodes: list) -> str:
        complexities = []
        for node in nodes:
            if isinstance(node, ast.AST):
                complexities.append(self.analyze_node(node))
        
        if 'O(n³)' in complexities:
            return 'O(n³)'
        elif 'O(n²)' in complexities:
            return 'O(n²)'
        elif 'O(n log n)' in complexities:
            return 'O(n log n)'
        elif 'O(n)' in complexities:
            return 'O(n)'
        return 'O(1)'

    def analyze_source(self, source_code: str) -> Dict[str, Any]:
        """Analyze source code string directly."""
        try:
            tree = ast.parse(source_code)
            if isinstance(tree.body[0], ast.FunctionDef):
                func_node = tree.body[0]
                return {
                    'name': func_node.name,
                    'complexity': self.analyze_node_list(func_node.body),
                    'source': source_code
                }
            return {
                'name': 'unknown',
                'complexity': self.analyze_node_list(tree.body),
                'source': source_code
            }
        except Exception as e:
            return {
                'name': 'unknown',
                'complexity': 'Error analyzing',
                'error': str(e),
                'source': source_code
            }

class ComplexityImporter:
    def __init__(self):
        self.analyzer = ComplexityAnalyzer()
        
    def analyze_module(self, module_name: str) -> Dict[str, Any]:
        try:
            module = __import__(module_name)
            results = {}
            
            for name, obj in inspect.getmembers(module):
                if inspect.isfunction(obj):
                    source = inspect.getsource(obj)
                    results[name] = self.analyzer.analyze_source(source)
                        
            return results
        
        except ImportError as e:
            return {'error': f'Failed to import module: {str(e)}'}

def install_analyzer():
    importer = ComplexityImporter()
    sys.modules['complexity_analyzer'] = importer
    return importer