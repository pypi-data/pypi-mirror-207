import typer
import jinja2 as jj
import typer_tinydb as ttdb
import shutil

from pathlib import Path
from flask import send_from_directory, Flask, make_response, render_template
from pytube import YouTube

Pkg = Path(__file__).parent
Root = Pkg.parent
Assets = Root / 'assets'
cssTemplateFile = Assets / 'style.css.tpl'
htmlTemplateFile = Assets / 'index.html.tpl'

app = typer.Typer(
    name="vidshare",
    help="Quickly make a small website to share one video, with a card and your name on it + description.",
    no_args_is_help=True,
    rich_help_panel='rich',
    rich_markup_mode='rich'
)

info = ttdb.cfg.registered_commands

app.add_typer(ttdb.cfg, name="var", add_help_option=True)

VARIABLES = [
    'background_image_url',
    'profile_picture_url',
    'video_url',
    'github_repo',
    'twitter_handle'
]

DEFAULTS = [
    "https://i.imgur.com/ThKEz2i.png",
    "https://imgur.com/uKXnoi0",
    "https://www.youtube.com/embed/dQw4w9WgXcQ",
    '#',
    '#'
]

DEFAULT_BUILD_DIR = Path().home() / '.vidcardshare'
DEFAULT_BUILD_PATH = DEFAULT_BUILD_DIR / 'video-website'
DEFAULT_BUILD_PATH.mkdir(parents=True, exist_ok=True)

def attemptGetVarsDB(*vars, **kwargs):
    """Checks the variables have been declared"""
    return {
        var : ttdb.getValue(var) for var in vars
    } | kwargs
    
def promptVarsMissing(**variables):
    missing = "[bold red]🚩 There are missing variables:[/bold red]\n"
    okay = "[bold green]✅ The following variables are correctly set:[/bold green]\n"
    defaults = "[bold yellow]📦 The following variables are set to the default package value:[/bold yellow]\n"
    misses, oks, defts = False, False, False
    for i, (name, val) in enumerate(variables.items()):
        if not val:
            misses = True
            missing += f'[red]({i}) {name}\n[/red]'
        elif val in DEFAULTS:
            defts = True
            defaults += f'[yellow]({i}) {name} (with value = [dim]{val}[/dim])\n[/yellow]'
        else:
            oks = True
            okay += f'[green]({i}) {name} (with value = [dim]{val}[/dim])\n[/green]'
        
    rets = ''
    rets += missing if misses else ''
    rets += defaults if defts else ''
    rets += okay if oks else ''
    return misses, rets


@app.command("build", help="""Assuming every parameter was provided, gives you a single zipped archive with your mini website in it. Just put it wherever :)\n❗ [red] Don't miss out ! [/red] you can also add build parameters using [yellow]`var set`[/yellow], type [yellow]`vidshare var`[/yellow] to know more !""")
def build(
        background_image_url: str = typer.Argument(
            default="https://storage.googleapis.com/open.data.arnov.dev/static/branding/topo-bright.png",
            show_default=False,
            help="Background image behind the card, defaults to [link=https://storage.googleapis.com/open.data.arnov.dev/static/branding/topo-bright.png]one picture I like[/link]"
        ),
        profile_picture_url: str = typer.Argument(
            default="https://static.wikia.nocookie.net/picrewcomp/images/4/44/Sangled.png/revision/latest?cb=20210731025719",
            show_default=False,
            help="Background image behind the card, defaults to [link=https://static.wikia.nocookie.net/picrewcomp/images/4/44/Sangled.png/revision/latest?cb=20210731025719]a random avatar from picrew.me[/link]"
        ),
        video_url: str = typer.Argument(
            default="https://www.youtube.com/embed/dQw4w9WgXcQ",
            show_default=False,
            help="Background image behind the card, defaults to [link=https://www.youtube.com/embed/dQw4w9WgXcQ]a super secret video[/link]"
        ),
        github_repo: str = typer.Option(
            '#',
            '-ghr', '--github-repo',
            show_default=False,
            help="Just your github repo, <user>/<repo>"
        ),
        twitter_handle: str = typer.Option(
            '#',
            '-tw', '--twitter-handle',
            show_default=False,
            help="Just your twitter handle, without the @ (ex: @joe => joe)"
        ),
        out_path: Path = typer.Option(
            DEFAULT_BUILD_PATH,
            '-o', '--out-dir',
            help="Where to output the zipped website"
        ),
        youtube_quality: int = typer.Option(
            1080,
            '-yq', '--youtube-quality',
            help="If your link is a youtube link, what quality to download it in."
        ),
        keep_archive_only: bool = typer.Option(
            False,
            '-k', '--keep-archive-only', help="Whether to remove everything but the archive after build."
        )            
    ):

    variables = attemptGetVarsDB(*VARIABLES, background_image_url=background_image_url, profile_picture_url=profile_picture_url, video_url=video_url, github_repo=github_repo, twitter_handle=twitter_handle)
    missing, message = promptVarsMissing(**variables)
    
    video = variables['video_url']
    pic = variables['profile_picture_url']
    bg = variables['background_image_url']
    
    names = [
            'background_image_url',
            'profile_picture_url',
            'video_url',
        ]
    
    if missing:
        ttdb.console.print(message)
        typer.Exit(1)
    else:
        for item, name in zip([bg, pic, video], names):
            if (pitm := Path(item)).is_file():
                variables[name] = pitm.name
            elif 'www.youtube.com' in item:
                ttdb.console.print(f"📦 Downloading youtube video in {youtube_quality}p quality", style='yellow')
                yt = YouTube(item).streams.filter(progressive=True, file_extension='mp4').get_by_resolution(f"{youtube_quality}p")
                if yt:
                    yt.download(filename=f"{name}_youtube.mp4")
                else:
                    anyvid = YouTube(item).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()               
                    anyvid.download(filename=f"{name}_youtube.mp4")
                ttdb.upsert_param(name, f"{name}_youtube.mp4")
                video = f"{name}_youtube.mp4"
                variables['video_url'] = video
        ttdb.console.print("✅[green] All variables set.[/green][yellow] Let's build ! 🚀[/yellow]")
        cssTpl = jj.Template(cssTemplateFile.read_text()).render(variables)
        htmlTpl = jj.Template(htmlTemplateFile.read_text()).render(variables)
        base = out_path.parent
        archive = out_path.stem
        root = out_path.parent / out_path.stem if out_path.suffix else out_path
        fmt = out_path.suffix.replace('.','') or 'zip'
        root.mkdir(exist_ok=True)
        (root / 'index.html').write_text(htmlTpl)
        (root / 'style.css').write_text(cssTpl)
        shutil.copyfile(Assets/'script.js', root / 'script.js')
        for item in [bg, pic, video]:
            if (pitm := Path(item)).is_file():
                shutil.copyfile(pitm, root / pitm.name)
        shutil.make_archive(base_dir=base,base_name=archive, root_dir=root, format=fmt)
        ttdb.console.print(f"✅[green] Built archive at {root}")
        if keep_archive_only:
            shutil.rmtree(root)
        for vid in Path().cwd().glob("*.mp4"):
            vid.unlink()


@app.command("serve", help="""Serves your site locally, if you built it. Else attempts to build first, then serve.""")
def serve(
        out_path: Path = typer.Option(
            DEFAULT_BUILD_PATH,
            '-o', '--out-dir',
            help="Where to output the website files"
        ),
    ):
    server = Flask(
        root_path=out_path,
        import_name=__name__,
        static_folder="")
    if not out_path.exists():
        build(**dict(zip(VARIABLES, DEFAULTS)), youtube_quality=1080, out_path=out_path)
    
    @server.route('/<path:path>')
    def send_report(path):
        return send_from_directory(out_path, 'index.html')
    server.run(host='localhost', port=5000, debug=True)