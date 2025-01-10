import os

def get_testcases(script_path: str):
    """Generate the test cases

    Args:
        script_path (str): _description_

    Raises:
        FileNotFoundError: _description_
        FileNotFoundError: _description_
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
    """
    input_keyword="input" 
    output_keyword="output" 
    file_extension=".txt"
    Question = os.path.join(os.path.dirname(script_path))
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
    if "\\" in Question:
        Question = Question.split("\\")[-1]
    else:
        Question = Question.split("/")[-1]
    
    if "Questions" not in os.listdir(base_dir):
        raise FileNotFoundError(f"Could not find the directory named Question")
    else:
        QuestionPath = os.path.join(base_dir,"Questions")
    if Question not in os.listdir(QuestionPath):
        raise FileNotFoundError(f"Could not find the directory named {Question} in {QuestionPath}")
    else:
        QuestionPath = os.path.join(QuestionPath,Question)
    if input_keyword not in os.listdir(QuestionPath) and output_keyword not in os.listdir(QuestionPath):
        raise FileNotFoundError(f"Could not find directories containing '{input_keyword}' or '{output_keyword}' in {QuestionPath}.")
    else:
        input_dir = os.path.join(QuestionPath,input_keyword)
        output_dir = os.path.join(QuestionPath,output_keyword)
    input_files = [file for file in os.listdir(input_dir) if file.endswith(file_extension)]
    testcases = {
        os.path.join(input_dir, file): os.path.join(output_dir, file.replace(input_keyword, output_keyword))
        for file in input_files
    }
    return testcases

def validator(result,output):
    """Validate the test case

    Args:
        result (_type_): _description_
        output (_type_): _description_

    Returns:
        _type_: _description_
    """
    file = open(output)
    expected = list(map(int,file.readline().strip().split()))
    if result == expected:
        return f"Test Case Passed with Result {result} where expected is {expected}"
    else:
        return f"Test Case Failed expected is {expected}"
    file.close()

