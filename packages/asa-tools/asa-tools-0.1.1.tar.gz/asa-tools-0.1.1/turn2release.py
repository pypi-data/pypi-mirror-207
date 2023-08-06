import click
import shutil
from pathlib import Path
import re

@click.group()
def cli():
    pass

@click.command()
@click.argument('source')
def ra(source):
    """
    removeAnnotate  去掉注解
    """
    folder_path = Path(source)  # 替换为文件夹实际路径
    files = folder_path.glob("**/*")  # 匹配文件夹下所有文件，包括子目录中的文件
    for file in files:
        file_extension = file.suffix
        if file_extension == '.py':
            with open(file, 'r', encoding='utf-8') as f:
                contents = f.read()
                # (?m)多行匹配  \s匹配空格或制表符  #后匹配空格，为了避免有些md5被去掉
                contents = re.sub(r'(?m)\s*#\s.*\n?', '\n', contents)
                contents = re.sub(
                    r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', contents)
                contents = contents.replace('\n\n', '\n')    # 去掉连续换行
                contents = re.sub(r'^\n', '', contents)      # 去掉换行开头的
            with open(file, 'w', encoding='utf-8') as f:
                f.write(contents)
            print("转换文件", file)  # 打印文件路径

@click.command()
@click.argument('source')
def cf(source):
    """
    copyFolder
    """
    src_folder = source
    dst_folder = source+'_copy'
    shutil.copytree(src_folder, dst_folder)

cli.add_command(ra)
cli.add_command(cf)

