import shutil
input_file = 'all.dot'
for name in ['lib1', 'lib2', 'exe1', 'exe2']:
    for extension in ['-uses']:
        output_file = name + extension + '.dot'
        print(output_file)
        shutil.copy(input_file, output_file)
