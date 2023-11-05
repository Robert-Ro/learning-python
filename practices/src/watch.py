from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import glob


path_to_watch = "."  # Change this to the path of the file you want to watch


def get_c_files(path):
    c_files = []
    for file in glob.glob(f"{path}/*.c"):
        c_files.append(file)
    return c_files


files = get_c_files(path_to_watch)


class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            # print(f"File {file_path} has been modified")
            file_name = file_path.split("/")[-1:][0]
            name = file_name.split(".")[0]
            extension = file_name.split(".")[-1:][0].lower()
            # print(file_name, extension, name)
            if extension == "c":
                # print(f"{file_name} file changed")
                print("gcc compiling...")
                # 执行系统命令，并获取输出
                commands = [
                    "gcc",
                    "-shared",
                    "-o",
                    "../output/demo.dylib",
                    "-fPIC",
                ] + files
                subprocess.run(
                    commands,
                    capture_output=True,
                    text=True,
                    cwd=".",
                )

    def on_created(self, event):
        print("file created")


def watch_for_modifications(path):
    event_handler = FileModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    watch_for_modifications(path_to_watch)
