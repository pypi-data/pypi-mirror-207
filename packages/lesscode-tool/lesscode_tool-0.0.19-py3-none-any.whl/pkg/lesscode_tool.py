"""
低代码构建工具.

Usage:
  lesscodeTool (new -d dir [-p project]|sqlacodegen -u url [-s schemas][-t tables][-f file][-i ignore]|subcommand -c command)

Options:
  -h, --help               查看帮助
  -v, --version            展示版本号
  -d, --dir dir            项目目录
  -u, --url url            数据库连接
  -f, --file file          表结构类输出文件
  -p, --project project    项目模板名
  -t, --tables tables      表名，用英文逗号连接多个表
  -s, --schemas schemas    库名，用英文逗号连接多个库
  -c, --command command    执行系统命令
  -i, --ignore ignore      生成model不带库名
"""
import os

from docopt import docopt

from pkg.tool.new import create_lesscode_project
from pkg.tool.sqlacodegen import sqlacodegen
from pkg.version import __version__


def main():
    arguments = docopt(__doc__, version=__version__)
    new_command_flag = arguments.get("new")
    sqlacodegen_command_flag = arguments.get("sqlacodegen")
    subcommand_flag = arguments.get("subcommand")
    if new_command_flag:
        project = arguments.get("--project")
        project_dir = arguments.get("--dir")
        if project is None:
            project = "lesscode-py"
        if project == "lesscode-py":
            create_lesscode_project(project_dir)
    elif sqlacodegen_command_flag:
        url = arguments.get("--url")
        file = arguments.get("--file")
        schema = arguments.get("--schemas")
        table = arguments.get("--tables")
        ignore = arguments.get("--ignore")
        if ignore is None:
            ignore = False
        else:
            if ignore in ["1", "True", "true", "是"]:
                ignore = True
            else:
                ignore = False
        schemas = None
        tables = None
        if schema is not None:
            schemas = schema.split(",")
        if table is not None:
            tables = table.split(",")
        sqlacodegen(url, schemas, tables, file, ignore)
    elif subcommand_flag:
        command = arguments.get("--command")
        os.system(command)


if __name__ == '__main__':
    main()
