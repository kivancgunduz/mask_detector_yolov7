import os
import shutil



def split_with_list(test_data_path: str, images_path:str, labels_path:str) -> None:
    """
    Move data according to test.txt
    :param test_data_path: path to test.txt
    :return: None
    """
    with open(test_data_path, 'r') as f:
        # read file path from test.txt
        print('starting move data')
        file_count = 0
        for line in f:
            # read file path from test.txt
            line = line.strip()
            root_directory = line.split('/')[-2]
            file_name = line.split('/')[-1]
            file_path = os.path.join(root_directory + '/' + file_name)
            # move matched files from directory to val/images folder
            shutil.move(file_path, images_path)
            # find corresponding txt file and move it to val/labels folder
            file_without_extension = file_name.split('.')[0]
            txt_file_path = os.path.join(root_directory + '/' + file_without_extension + '.txt')
            shutil.move(txt_file_path, labels_path)
            file_count += 1
        print(f'{file_count} images moved.')

def split_image_txt(data_path: str, images_path: str, labels_path:str) -> None:
    """
    Split source folder into image and labels
    :param data_path: path to source folder
    :return: None
    """
    print('starting move data')
    file_count = 0
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith('.jpg'):
                # move matched files from directory to target images folder
                shutil.move(os.path.join(root, file), images_path)
                # find corresponding txt file and move it to target labels folder
                file_without_extension = file.split('.')[0]
                txt_file_path = os.path.join(root, file_without_extension + '.txt')
                shutil.move(txt_file_path, labels_path)
                file_count += 1
    print(f'{file_count} images moved.')


if __name__ == '__main__':
    #test_data_path = 'test.txt'
    #split_image_txt(test_data_path)
    split_image_txt('obj', 'train/images', 'train/labels')
    print('Done')
