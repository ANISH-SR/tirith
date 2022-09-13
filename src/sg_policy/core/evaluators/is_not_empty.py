from .base_evaluator import BaseEvaluator

# Checks if input is not empty

# Args:
#     value (mixed): Value to check.

# Returns:
#     bool: Whether :attr:`value` is not empty

# Example:

#     >>> e('')
#     False
#     >>> e("abc")
#     True
#     >>> l([])
#     False

# .. versionadded:: 1.0.0-alpha.1


class IsNotEmpty(BaseEvaluator):
    def evaluate(self, evaluator_input, evaluator_data = None):
        input = evaluator_input
        evaluation_result = {"passed": False, "message": "Not evaluated"}
        try:
            if (isinstance(input, str) or isinstance(input, list) or isinstance(input, dict)) and input:
                evaluation_result["passed"] = True
                evaluation_result["message"] = "{} is not empty".format(input)
            if not evaluation_result["passed"]:
                evaluation_result["message"] = "{} is empty".format(input)
            return evaluation_result
        except Exception as e:
            evaluation_result["message"] = str(e)
            return evaluation_result
