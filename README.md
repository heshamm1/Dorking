# Google Dorking Tool

```
██████╗  ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██║  ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║  ██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        Google Dorking Tool - By sh1vv
                Use Responsibly!
```

A powerful and customizable Python tool for automating Google dorking queries using the **Google Custom Search JSON API**. This tool allows you to perform advanced searches on a target domain or wildcard, making it ideal for security researchers, penetration testers, and bug bounty hunters.

---

## Features

- **Automated Google Dorking**: Run multiple dork queries on a target domain or wildcard.
- **Colorful Output**: Displays results in a visually appealing format with colored tables and progress bars.
- **Rich Results**: Shows the title, URL, and snippet of each search result for better context.
- **Rate Limiting Avoidance**: Includes random delays between queries to avoid hitting Google's rate limits.
- **Customizable**: Easily add or modify dork queries in the `dorks.py` file.

---

## Prerequisites

Before using this tool, ensure you have the following:

1. **Google API Key**:
   - Create a Google Cloud project and enable the **Custom Search JSON API**.
   - Generate an API key from the [Google Cloud Console](https://console.cloud.google.com/).

2. **Custom Search Engine (CSE) ID**:
   - Create a Custom Search Engine at [Google Programmable Search Engine](https://programmablesearchengine.google.com/about/).
   - Configure the CSE to search the entire web or specific domains.

3. **Python 3.7+**: Ensure Python is installed on your system.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/google-dorking-tool.git
   cd google-dorking-tool
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the tool with the following command-line options:
### Basic Usage
```
python google_dorking_tool.py -d example.com
```
> -d or --domain: Specify the target domain (e.g., example.com).

### Wildcard Search
```
python google_dorking_tool.py -w *.example.com
```
> -w or --wildcard: Specify a wildcard target (e.g., *.example.com).

### Example output
```
██████╗  ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██║  ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║  ██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
          Google Dorking Tool - By sh1vv
                  Use Responsibly!

Starting search for target: example.com

[*] Searching for: site:example.com filetype:pdf
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Title                                ┃ URL                                  ┃ Snippet                              ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Example Document 1                   │ https://example.com/document1.pdf    │ This is a sample PDF document.       │
│ Example Document 2                   │ https://example.com/document2.pdf    │ Another sample PDF document.        │
└──────────────────────────────────────┴──────────────────────────────────────┴──────────────────────────────────────┘
Sleeping for 12.34 seconds...
--------------------------------------------------
```
## Configuration
### Adding Dorks
You can add or modify dork queries in the dorks.py file. Example:
```
GOOGLE_DORKS = [
    "site:{target} filetype:pdf",
    "site:{target} intitle:admin",
    "site:{target} inurl:login",
    "site:{target} ext:php",
]
```
