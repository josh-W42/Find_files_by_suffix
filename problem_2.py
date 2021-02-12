import os

def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix of the file name to be found
    path(str): path of the file system

  Returns:
      a list of absolute paths
  """
  if type(suffix) != str or type(path) != str:
    raise TypeError('Args need to be of type: str')
  elif suffix == '' or path == '':
    raise ValueError('Args must be non-empty strings')
  
  output = list()
  curent_dir_files = []

  if os.path.isdir(path):
    curent_dir_files = os.listdir(path)
  elif os.path.isfile(path):
    if path.endswith(suffix):
      output.append(path)
    else:
      return []
  else:
    print('Not a valid path')
    return []


  for string in curent_dir_files:
    path_to_obj = os.path.join(path, string)

    # determine if it's a file
    if not os.path.isfile(path_to_obj):

    # non-files are directories we must traverse
      output += find_files(suffix, path_to_obj)
    
    else:
      # determine if it's a file we're looking for.
      if path_to_obj.endswith(suffix):

        # Add to our output list
        output.append(path_to_obj)

  return output

def test_suite():
  '''Performs a series of tests on the find_files function'''
  
  print('\nBasic Function Tests \n')

  print('Function With Empty input Test', end=' ')
  try:
    find_files('', '')
  except ValueError:
    print('pass')
  else:
    print('Fail')

  print('Function With Null input Test', end=' ')
  try:
    find_files(None, None)
  except TypeError:
    print('pass')
  else:
    print('Fail')

  current_dir_path =  os.path.dirname(os.path.abspath(__file__))

  print('Function with path to a file Test:', end=' ')

  path_to_current_file = os.path.join(current_dir_path, 'problem_2.py')

  test_solution = [path_to_current_file]
  test_answer = find_files(".py", path_to_current_file)

  has_passed = True

  if len(test_answer) == 0:
    has_passed = False
  else:
    for item in test_answer:
      if not item in test_solution:
        has_passed = False

  if has_passed:
    print('pass')
  else:
    print('Fail')

  print('Function With Given Directory Test:', end=' ')

  test_solution = list()

  # While this does solve the same problem, it looks like alot of the hard work is done for me with os.walk.
  for root, dirs, files in os.walk('./testdir'):
    for file in files:
      if file.endswith('.c'):
        test_solution.append(os.path.join(os.path.join(current_dir_path,root[2:]), file))

  test_answer = find_files(".c", current_dir_path)

  has_passed = True

  if len(test_answer) == 0:
    has_passed = False
  else:
    for item in test_solution:
      if not (item in test_answer):
        has_passed = False

  if has_passed:
    print('pass')
  else:
    print('Fail')

  


if __name__ == "__main__":
    test_suite()