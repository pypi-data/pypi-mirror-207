import click
from pyxk.m3u8downloader import load_url, load_content



@click.group(invoke_without_command=True)
@click.option("-u", "--url", "url", type=str, default=None, help="m3u8 url")
@click.option("-o", "--output", "output", type=str, default=None, help="M3U8存储路径")
@click.option("--reload", is_flag=True, help="重载m3u8资源")
@click.option("--reserve", is_flag=True, help="保留m3u8资源")
@click.option("-h", "--headers", "headers", type=(str, str), multiple=True, help="Request Headers")
@click.option("--no-verify", "verify", is_flag=True, default=True, help="Request Verify")
@click.option("-l", "--limit", "limit", type=int, default=16, help="下载并发量")
@click.pass_context
def main(ctx, url, output, reload, reserve, headers, verify, limit):
    """下载m3u8资源 - m3u8 url"""
    if not ctx.obj or not isinstance(ctx.obj, dict):
        ctx.obj = {}
    # 将参数传递给子命令
    if ctx.invoked_subcommand:
        ctx.obj.update(ctx.params)
        return
    # 没有调用子命令
    if not url:
        url = click.prompt("请输入 m3u8 url", type=str)
    load_url(url, output=output, reload=reload, reserve=reserve, headers=dict(headers), verify=verify, limit=limit)

@main.command
@click.pass_obj
@click.argument("content", type=click.Path(exists=True), metavar="<m3u8 file path>")
@click.option("-u", "--url", "url", type=str, default=None, help="m3u8 url")
@click.option("-o", "--output", "output", type=str, default=None, help="M3U8存储路径")
@click.option("--reload", is_flag=True, help="重载m3u8资源")
@click.option("--reserve", is_flag=True, help="保留m3u8资源")
@click.option("-h", "--headers", "headers", type=(str, str), multiple=True, help="Request Headers")
@click.option("--no-verify", "verify", is_flag=True, default=True, help="Request Verify")
@click.option("-l", "--limit", "limit", type=int, default=None, help="下载并发量")
def file(obj, content, url, output, reload, reserve, headers, verify, limit):
    """下载m3u8资源 - m3u8 content"""
    load_content(
        content=content,
        url=url or obj["url"],
        output=output or obj["output"],
        reload=reload,
        reserve=reserve,
        headers=dict(headers or obj["headers"]),
        verify=verify,
        limit=limit or obj["limit"]
    )
