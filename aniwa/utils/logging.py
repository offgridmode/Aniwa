"""Logging and verbosity management for Aniwa."""

from enum import Enum
from typing import Any, Optional
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import sys


class VerbosityLevel(str, Enum):
    """Verbosity levels for controlling output visibility."""
    
    QUIET = "quiet"      # Only critical errors and final status
    NORMAL = "normal"    # Default: standard profiling messages
    VERBOSE = "verbose"  # Detailed progress and timing
    DEBUG = "debug"      # Internal diagnostics and debugging


class AniwaLogger:
    """Central logging manager for Aniwa."""
    
    def __init__(self, verbosity: VerbosityLevel = VerbosityLevel.NORMAL):
        """Initialize logger with verbosity level.
        
        Args:
            verbosity: Level of output detail to show
        """
        self.verbosity = verbosity
        self.console = Console()
        self._debug_enabled = verbosity == VerbosityLevel.DEBUG
        self._verbose_enabled = verbosity in [VerbosityLevel.VERBOSE, VerbosityLevel.DEBUG]
        self._quiet_enabled = verbosity == VerbosityLevel.QUIET
    
    def set_verbosity(self, verbosity: VerbosityLevel):
        """Update verbosity level at runtime."""
        self.verbosity = verbosity
        self._debug_enabled = verbosity == VerbosityLevel.DEBUG
        self._verbose_enabled = verbosity in [VerbosityLevel.VERBOSE, VerbosityLevel.DEBUG]
        self._quiet_enabled = verbosity == VerbosityLevel.QUIET
    
    def info(self, message: str, icon: str = "→"):
        """Show informational message (normal and above)."""
        if not self._quiet_enabled:
            self.console.print(f"[bold blue]{icon}[/bold blue] {message}")
    
    def success(self, message: str, icon: str = "✓"):
        """Show success message (normal and above)."""
        if not self._quiet_enabled:
            self.console.print(f"[bold green]{icon}[/bold green] {message}")
    
    def warning(self, message: str, icon: str = "⚠"):
        """Show warning message (normal and above)."""
        if not self._quiet_enabled:
            self.console.print(f"[bold yellow]{icon}[/bold yellow] {message}")
    
    def error(self, message: str, icon: str = "✗"):
        """Show error message (always shown)."""
        self.console.print(f"[bold red]{icon}[/bold red] {message}")
    
    def verbose(self, message: str, icon: str = "→"):
        """Show verbose message (verbose or debug mode)."""
        if self._verbose_enabled:
            self.console.print(f"[dim]{icon}[/dim] {message}")
    
    def debug(self, message: str, data: Optional[Any] = None):
        """Show debug message with optional data (debug mode only)."""
        if self._debug_enabled:
            if data:
                self.console.print(f"[dim cyan][DEBUG][/dim cyan] {message}")
                if isinstance(data, dict):
                    for key, value in data.items():
                        self.console.print(f"[dim cyan]  {key}:[/dim cyan] {value}")
                elif isinstance(data, (list, tuple)):
                    for item in data[:10]:  # Limit to first 10 items
                        self.console.print(f"[dim cyan]  •[/dim cyan] {item}")
                    if len(data) > 10:
                        self.console.print(f"[dim cyan]  ... and {len(data)-10} more[/dim cyan]")
                else:
                    self.console.print(f"[dim cyan]  {data}[/dim cyan]")
            else:
                self.console.print(f"[dim cyan][DEBUG][/dim cyan] {message}")
    
    def debug_panel(self, title: str, content: Any, language: str = "yaml"):
        """Show debug information in a panel (debug mode only)."""
        if self._debug_enabled:
            content_str = str(content)
            syntax = Syntax(content_str, language, theme="monokai", line_numbers=False)
            panel = Panel(syntax, title=f"[cyan]DEBUG: {title}[/cyan]", border_style="cyan")
            self.console.print(panel)
    
    def stage(self, name: str, level: VerbosityLevel = VerbosityLevel.VERBOSE):
        """Context manager for stage indication."""
        class StageContext:
            def __enter__(self_ctx):
                if level == VerbosityLevel.VERBOSE and self._verbose_enabled:
                    self.console.print(f"[bold blue]→[/bold blue] {name}...")
                elif level == VerbosityLevel.DEBUG and self._debug_enabled:
                    self.console.print(f"[dim cyan][DEBUG][/dim cyan] Entering stage: {name}")
                return self_ctx
            
            def __exit__(self_ctx, *args):
                if level == VerbosityLevel.VERBOSE and self._verbose_enabled:
                    self.console.print(f"[dim]  ✓ {name} complete[/dim]")
                elif level == VerbosityLevel.DEBUG and self._debug_enabled:
                    self.console.print(f"[dim cyan][DEBUG][/dim cyan] Exiting stage: {name}")
        
        return StageContext()
    
    def timing(self, operation: str, duration: float):
        """Show timing information (verbose and debug modes)."""
        if self._verbose_enabled:
            if duration < 0.001:
                time_str = f"{duration*1000000:.0f}µs"
            elif duration < 0.01:
                time_str = f"{duration*1000:.2f}ms"
            elif duration < 1:
                time_str = f"{duration*1000:.0f}ms"
            else:
                time_str = f"{duration:.2f}s"
            self.verbose(f"{operation} completed in {time_str}", icon="⏱")


# Global logger instance (will be configured in CLI)
_logger: Optional[AniwaLogger] = None


def get_logger() -> AniwaLogger:
    """Get the global logger instance."""
    global _logger
    if _logger is None:
        _logger = AniwaLogger()
    return _logger


def configure_logger(verbosity: VerbosityLevel):
    """Configure the global logger with verbosity level."""
    global _logger
    _logger = AniwaLogger(verbosity)


def log_info(message: str, icon: str = "→"):
    """Log informational message."""
    get_logger().info(message, icon)


def log_success(message: str, icon: str = "✓"):
    """Log success message."""
    get_logger().success(message, icon)


def log_warning(message: str, icon: str = "⚠"):
    """Log warning message."""
    get_logger().warning(message, icon)


def log_error(message: str, icon: str = "✗"):
    """Log error message."""
    get_logger().error(message, icon)


def log_verbose(message: str, icon: str = "→"):
    """Log verbose message."""
    get_logger().verbose(message, icon)


def log_debug(message: str, data: Any = None):
    """Log debug message."""
    get_logger().debug(message, data)


def log_stage(name: str):
    """Context manager for stage logging."""
    return get_logger().stage(name)