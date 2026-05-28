"""Progress tracking utilities for Aniwa."""

from contextlib import contextmanager
from time import perf_counter
from typing import Optional
from rich.console import Console
from rich.status import Status


console = Console()


class ProgressTracker:
    """Central progress tracking for profiling operations.
    
    Provides context managers for tracking execution time and progress
    of various profiling stages.
    """
    
    def __init__(self, verbose: bool = False):
        """Initialize progress tracker.
        
        Args:
            verbose: If True, show detailed progress information
        """
        self.verbose = verbose
        self.timings = {}
    
    @contextmanager
    def stage(self, name: str, total_steps: Optional[int] = None):
        """Context manager for profiling stages with timing.
        
        Args:
            name: Name of the stage for display
            total_steps: Optional - not used in this version, kept for API compatibility
        
        Yields:
            None or a callback function (kept for API compatibility)
        """
        start = perf_counter()
        
        if self.verbose:
            console.print(f"[bold blue] {name}...[/bold blue]")
            try:
                # Yield a dummy callback for API compatibility with profiler.py
                def dummy_callback(advance: int = 1):
                    pass
                yield dummy_callback
            finally:
                elapsed = perf_counter() - start
                self.timings[name] = elapsed
                # Format duration appropriately
                if elapsed < 0.01:
                    time_str = f"{elapsed*1000:.2f}ms"
                else:
                    time_str = f"{elapsed:.2f}s"
                console.print(f"[dim]   Completed in {time_str}[/dim]")
        else:
            try:
                yield None
            finally:
                elapsed = perf_counter() - start
                self.timings[name] = elapsed
    
    def show_timing_summary(self):
        """Display all timing information if verbose mode is enabled."""
        if self.verbose and self.timings:
            console.print("\n[bold cyan]Timing Summary:[/bold cyan]")
            for stage, duration in self.timings.items():
                # Format duration with appropriate precision
                if duration < 0.01:
                    time_str = f"{duration*1000:.2f}ms"
                else:
                    time_str = f"{duration:.2f}s"
                console.print(f"  {stage}: {time_str}")
    
    def reset(self):
        """Reset all timing data."""
        self.timings = {}