auto_quant_trader/
├── README.md
├── .env.example
├── main.py
├── config/
│   └── settings.py
├── crawler/
│   ├── __init__.py
│   ├── arxiv_scraper.py
│   ├── blog_scraper.py
│   ├── reddit_scraper.py
│   ├── ssrn_scraper.py
│   ├── semantic_scholar_scraper.py
│   ├── medium_scraper.py
│   ├── github_scraper.py
│   └── universal_fetcher.py
├── llm/
│   ├── __init__.py
│   ├── strategy_extractor.py
│   └── prompts/
│       └── extract_strategy.txt
├── strategies/
│   ├── __init__.py
│   └── generated/
│       └── strategy_template.py
├── backtester/
│   ├── __init__.py
│   ├── evaluate.py
│   └── metrics.py
├── deployer/
│   ├── __init__.py
│   ├── save_to_git.py
│   ├── alpaca_deploy.py
│   └── logger.py
└── utils/
    ├── __init__.py
    ├── file_utils.py
    └── data_loader.py
