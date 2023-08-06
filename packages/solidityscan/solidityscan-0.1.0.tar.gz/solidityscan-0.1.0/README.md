## solscan

## Installation
`pip install solscan`
> todo: add platform dependent binary sources

## Commands

### `config`
  1. `add-update-config`
      a. --token (token for authentication)
      b. --error-language (language for the error messages)
  2. `show-config-path`
      > show path of config file
  
### `scan`
  1. `--scan-type=<scan_type>`
      > supported scan_types = "project" or "block"
      
      - `project` scan_type required parameters
        - -project-url
        - -project-branch
        - -project-name
				- -skip-file-paths
				- -rescan
      - `block` scan_type required parameters
        - -contract-address
        - -contract-platform
        - -contract-chain

## Error Codes
1. 000x - Errors raised by the server
2. 100x - Errors raised by the SDK
