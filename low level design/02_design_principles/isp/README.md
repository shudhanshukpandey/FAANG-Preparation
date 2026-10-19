# Interface Segregation Principle (ISP)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Definition**: "Clients should not be forced to depend upon interfaces or methods that they do not use."
- **Fat Interface (Anti-Pattern)**: An interface bloated with 10 different methods. A simple class implementing it is forced to provide empty dummy stubs or raise `NotImplementedError` for methods it doesn't support.
- **Rule of Thumb**: Prefer many small, client-specific role interfaces over one large general-purpose interface.

## Architecture & Data Flow

```mermaid
classDiagram
    subgraph AntiPattern [Fat Interface Violating ISP]
        class IMachine {
            +print_doc()
            +scan_doc()
            +fax_doc()
        }
        class OldPrinter {
            +print_doc()
            +scan_doc() throws Error!
            +fax_doc() throws Error!
        }
        IMachine <|.. OldPrinter
    end

    subgraph CleanISP [Role Interfaces Complying with ISP]
        class IPrinter {
            +print_doc()
        }
        class IScanner {
            +scan_doc()
        }
        class IFax {
            +fax_doc()
        }
        class SimpleInkjetPrinter {
            +print_doc()
        }
        class OfficeAllInOne {
            +print_doc()
            +scan_doc()
            +fax_doc()
        }

        IPrinter <|.. SimpleInkjetPrinter
        IPrinter <|.. OfficeAllInOne
        IScanner <|.. OfficeAllInOne
        IFax <|.. OfficeAllInOne
    end
```

## FAANG Interview Significance
- Keeps clients lean and decoupled.
- In Python, `typing.Protocol` with single or double methods (e.g. `Iterable`, `Closeable`, `Serializable`) makes interfaces highly composable.
