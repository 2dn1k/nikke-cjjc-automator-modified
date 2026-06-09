import sys
import typer
import traceback
from nikke_cjjc_automator.core import entry, NikkeAutomator
from nikke_cjjc_automator.view.menu import select_mode

app = typer.Typer(add_completion=False, no_args_is_help=False)

def entry_cli():
    NikkeAutomator.ensure_admin()
    args = [a for a in sys.argv[1:] if not a.endswith('.exe')]
    
    if not args or not any(a.startswith('-') or a.isdigit() for a in args):
        menu_result = NikkeAutomator.select_mode()
        
        if isinstance(menu_result, tuple):
            mode, is_top_8, custom_args = menu_result
        else:
            mode, is_top_8, custom_args = menu_result, False, None
            
        entry(mode, is_top_8=is_top_8, custom_args=custom_args)
        return
    app()

@app.command()
def run(mode: int = typer.Option(None, help="Run mode: 1=Prediction, 2=Review, 3=Anti-Buy")):
    is_top_8 = False
    custom_args = None
    
    if mode is None:
        menu_result = NikkeAutomator.select_mode()
        if isinstance(menu_result, tuple):
            mode, is_top_8, custom_args = menu_result
        else:
            mode = menu_result

    entry(mode, is_top_8=is_top_8, custom_args=custom_args)

if __name__ == "__main__":
    try:
        entry_cli()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        NikkeAutomator.notify_error(str(e))
        input("Press Enter to exit...")
        raise