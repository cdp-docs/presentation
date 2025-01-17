# CDP Presentation

## Setup

Install: `pip install mkdocs`

Build:

```
mkdocs serve
```

Access locally at http://127.0.0.1:8000/.

## Repo Structure

```
.
├── docs
│   ├── img
│   │   ├── cdp_portal.png
│   │   ├── sepolia.png
│   │   ├── setup.png
│   │   └── trust.mp4
│   ├── index.md
│   ├── tutorials
│   │   └── smart-contracts-101.md
│   └── welcome
│       ├── backend-create-wallet.md
│       └── getting-started.md
├── examples
│   ├── deploy_token.py
│   ├── game.py
│   └── test_wallet_seed.json
├── mkdocs.yml
├── README.md
```

### `mkdocs.yml`

Configuration, where nav is defined.

### Welcome 

Setup and getting started guides (i.e. API key configuration and creating and funding a wallet).

### Tutorials

I will probably end up moving my old blog posts over here one day, so I wrote this as a way to showcase other tutorials in the future.

The Smart Contracts 101 guide is what serves as my presentation assignment: https://cdp-docs.github.io/presentation/tutorials/smart-contracts-101/. 

### Code

The example game code can be found in [game.py](examples/game.py).
