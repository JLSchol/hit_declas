from pathlib import Path
import glob

import json

class ProjectPaths:
    def __init__(self):
        # get dirs
        self.root_dir = Path(__file__).parent.parent 
        self.config_dir = Path.joinpath(self.root_dir, "config")
        self.generated_dir = Path.joinpath(self.root_dir, "generated")
        self.logs_dir = Path.joinpath(self.root_dir, "logs")
        self.module_dir = Path(__file__).parent
        self.receits_dir = Path.joinpath(self.root_dir, "receits")
        self.dirs = [self.root_dir, self.config_dir, self.generated_dir, 
                        self.logs_dir, self.module_dir, self.receits_dir]

        # get all files within a dir (does not check)
        self.root_files = self.get_files(self.root_dir)
        self.config_files = self.get_files(self.config_dir)
        self.generated_files = self.get_files(self.generated_dir)
        self.logs_files = self.get_files(self.logs_dir)
        self.module_files = self.get_files(self.module_dir)
        self.receits_files = self.get_files(self.receits_dir)

        image_extenstions = [".PNG",".png",".JPG",".jpg",".JPEG",".jpeg", ".PDF",".pdf"]

        # get specific files (even if more is present)
        # config files
        self.personal_details = self.get_filetype(self.config_files, ".json")
        self.signature = self.get_filetype(self.config_files, image_extenstions)

        # receits
        self.receits = self.get_filetype(self.receits_files, image_extenstions)

    def get_files(self, abs_dir):
        return [f for f in Path.iterdir(abs_dir) if f.is_file()]

    def get_filetype(self, files, suffixes):
        suffixes = suffixes if isinstance(suffixes, list) else [suffixes]

        files_of_type = []
        for suffix in suffixes:
            files_of_type.extend([file for file in files if (file.suffix == suffix)])

        return files_of_type[0] if len(files_of_type) == 1 else files_of_type

    def show_dirs(self):
        print(f"1. root: {self.root_dir}")
        print(f"1.1 config: {self.config_dir}")
        print(f"1.2 generated: {self.generated_dir}")
        print(f"1.3 logs: {self.logs_dir}")
        print(f"1.4 modules: {self.module_dir}")
        print(f"1.5 receits: {self.receits_dir}")
        print()

    def show_files(self, files_in_dir=None):
        # if files from dirs is specified
        if files_in_dir != None:
            for i, file in enumerate(files_in_dir):
                print(f"{i}: {file.resolve()}")
        else: # print everything
            print_pretty = lambda text, file: print(f"{text} {file.resolve()}")
            [print_pretty("1 root:", file) for file in self.root_files]                
            [print_pretty("1.1 config:", file) for file in self.config_files]                
            [print_pretty("1.2 generated:", file) for file in self.generated_files]                
            [print_pretty("1.3 logs:", file) for file in self.logs_files]                
            [print_pretty("1.4 modules:", file) for file in self.module_files]    
            [print_pretty("1.4 receits:", file) for file in self.receits_files]    
        print()


class ImportJson:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.import_json(file_path)


    def file_exists(self, file_path):
        if Path.exists(file_path):
            return True
        else:
            print(f"file {file_path} does not exists!")
            return False

    def import_json(self, file_path):
        if self.file_exists(file_path):
            with open(file_path) as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
                return data


if __name__ == "__main__":
    p = ProjectPaths()
    # p.show_dirs()
    # p.show_files()

    data = ImportJson(p.personal_details).data
    # print(data)


