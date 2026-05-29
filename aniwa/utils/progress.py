"""Progress tracking utilities for Aniwa."""

from contextlib import contextmanager
from time import perf_counter
from typing import Optional
from rich.console import Console
from rich.progress import (
    Progress, 
    SpinnerColumn, 
    TextColumn, 
    BarColumn, 
    TimeElapsedColumn,
    TimeRemainingColumn
)
from aniwa.utils.logging import get_logger, VerbosityLevel


console = Console()


class ProgressTracker:
    """Central progress tracking for profiling operations."""
    
    def __init__(self, verbose: bool = False):
        """Initialize progress tracker.
        
        Args:
            verbose: If True, show detailed progress information
        """
        self.verbose = verbose
        self.timings = {}
        self._current_progress = None
        self._current_task = None
        self.logger = get_logger()
    
    @contextmanager
    def stage(self, name: str, total_steps: Optional[int] = None):
        """Context manager for profiling stages with visual progress bar.
        
        Args:
            name: Name of the stage for display
            total_steps: If provided, show progress bar with this many steps
        
        Yields:
            Optional callback function to advance progress bar
        """
        start = perf_counter()
        
        if self.verbose:
            if total_steps and total_steps > 0 and total_steps <= 1000:
                # Show progress bar for multi-step operations (reasonable size)
                with Progress(
                    TextColumn("[bold blue]{task.description}"),
                    BarColumn(bar_width=40),
                    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                    TimeElapsedColumn(),
                    TimeRemainingColumn(),
                    console=console,
                    transient=False,
                ) as progress:
                    task = progress.add_task(
                        f"{name}",
                        total=total_steps
                    )
                    
                    def progress_callback(advance: int = 1):
                        progress.advance(task, advance)
                    
                    try:
                        yield progress_callback
                    finally:
                        elapsed = perf_counter() - start
                        self.timings[name] = elapsed
                        # Show completion with timing
                        console.print(f"[dim]   {name} completed in {self._format_time(elapsed)}[/dim]")
            else:
                # Show indeterminate spinner for operations without steps
                # or when total_steps is too large (avoid performance issues)
                with Progress(
                    SpinnerColumn(),
                    TextColumn(f"[progress.description][bold blue]{name}...[/bold blue]"),
                    TimeElapsedColumn(),
                    console=console,
                    transient=True,
                ) as progress:
                    task = progress.add_task("", total=None)
                    try:
                        yield None
                    finally:
                        elapsed = perf_counter() - start
                        self.timings[name] = elapsed
                        console.print(f"[dim]   {name} completed in {self._format_time(elapsed)}[/dim]")
        else:
            # Non-verbose mode - just track timing, use logger for debug
            self.logger.debug(f"Stage started: {name}")
            try:
                yield None
            finally:
                elapsed = perf_counter() - start
                self.timings[name] = elapsed
                self.logger.debug(f"Stage completed: {name} in {self._format_time(elapsed)}")
    
    def _format_time(self, seconds: float) -> str:
        """Format time duration appropriately."""
        if seconds < 0.001:
            return f"{seconds*1000000:.0f}µs"
        elif seconds < 0.01:
            return f"{seconds*1000:.2f}ms"
        elif seconds < 1:
            return f"{seconds*1000:.0f}ms"
        else:
            return f"{seconds:.2f}s"
    
    def show_timing_summary(self):
        """Display all timing information if verbose mode is enabled."""
        if self.verbose and self.timings:
            console.print("\n[bold cyan]Timing Summary:[/bold cyan]")
            
            # Create a table for better visualization
            from rich.table import Table
            table = Table(show_header=True, header_style="bold cyan", box=None)
            table.add_column("Stage", style="cyan")
            table.add_column("Duration", justify="right", style="green")
            
            # Sort by duration (longest first) for better readability
            sorted_timings = sorted(self.timings.items(), key=lambda x: x[1], reverse=True)
            for stage, duration in sorted_timings:
                table.add_row(stage, self._format_time(duration))
            
            console.print(table)
            
            # Log total time to debug
            total_time = sum(self.timings.values())
            self.logger.debug(f"Total profiling time: {self._format_time(total_time)}")
    
    def reset(self):
        """Reset all timing data."""
        self.timings = {}


# Helper function for consistent time formatting (available globally)
def format_duration(seconds: float) -> str:
    """Format time duration appropriately (standalone function)."""
    if seconds < 0.001:
        return f"{seconds*1000000:.0f}µs"
    elif seconds < 0.01:
        return f"{seconds*1000:.2f}ms"
    elif seconds < 1:
        return f"{seconds*1000:.0f}ms"
    else:
        return f"{seconds:.2f}s"


# Helper context manager for simple operations
@contextmanager
def show_progress(message: str, verbose: bool = True):
    """Simple progress indicator for a single operation."""
    logger = get_logger()
    
    if verbose:
        console.print(f"[bold blue]→ {message}...[/bold blue]")
        start = perf_counter()
        try:
            yield
        finally:
            elapsed = perf_counter() - start
            if elapsed < 0.01:
                time_str = f"{elapsed*1000:.2f}ms"
            elif elapsed < 1:
                time_str = f"{elapsed*1000:.0f}ms"
            else:
                time_str = f"{elapsed:.2f}s"
            console.print(f"[dim]   Completed in {time_str}[/dim]")
            logger.debug(f"Operation completed: {message} in {time_str}")
    else:
        # Non-verbose mode - just log debug
        logger.debug(f"Operation: {message}")
        start = perf_counter()
        try:
            yield
        finally:
            elapsed = perf_counter() - start
            # Use the standalone format_duration function, not self._format_time
            logger.debug(f"Operation completed: {message} in {format_duration(elapsed)}")