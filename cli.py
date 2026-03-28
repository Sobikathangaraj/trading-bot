import typer
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs

load_dotenv()
app = typer.Typer()
console = Console()

@app.command()
def trade(
    symbol: str = typer.Option(..., help="e.g. BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Amount to trade"),
    price: float = typer.Option(None, help="Required for LIMIT orders"),
):
    errors = validate_inputs(symbol, side, order_type, quantity, price)
    if errors:
        for e in errors:
            console.print(f"[red]❌ {e}[/red]")
        raise typer.Exit(1)

    console.print("\n[bold cyan]📋 Order Summary[/bold cyan]")
    console.print(f"  Symbol   : {symbol.upper()}")
    console.print(f"  Side     : {side.upper()}")
    console.print(f"  Type     : {order_type.upper()}")
    console.print(f"  Quantity : {quantity}")
    if price:
        console.print(f"  Price    : {price}")

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = BinanceClient(api_key, api_secret)

    try:
        result = place_order(client, symbol, side, order_type, quantity, price)

        console.print("\n[bold green]✅ Order Placed Successfully![/bold green]")

        table = Table(title="Order Response")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="white")

        table.add_row("Order ID", str(result.get("orderId", "N/A")))
        table.add_row("Status", str(result.get("status", "N/A")))
        table.add_row("Executed Qty", str(result.get("executedQty", "N/A")))
        table.add_row("Avg Price", str(result.get("avgPrice", "N/A")))

        console.print(table)

    except Exception as e:
        console.print(f"\n[bold red]❌ Order Failed: {e}[/bold red]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()