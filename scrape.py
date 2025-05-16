'''Crawls + saves article text to data/coinbase_articles.json'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import json
import os
# few Coinbase Learn URLs
URLS = [
    "https://www.coinbase.com/learn/crypto-basics/what-is-cryptocurrency",
    "https://www.coinbase.com/learn/crypto-basics/what-is-bitcoin",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-blockchain",
    "https://www.coinbase.com/learn/crypto-basics/what-is-ethereum",
    "https://www.coinbase.com/learn/crypto-basics/how-to-secure-crypto",
    "https://www.coinbase.com/learn/crypto-basics/understanding-crypto-taxes",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-crypto-airdrop",
    "https://www.coinbase.com/learn/crypto-basics/what-are-ethereum-layer-2-blockchains-and-how-do-they-work",
    "https://www.coinbase.com/learn/crypto-basics/what-are-digital-assets",
    "https://www.coinbase.com/learn/crypto-basics/forex-trading-vs-crypto-which-is-right-for-you",
    "https://www.coinbase.com/learn/crypto-basics/what-is-nft-art",
    "https://www.coinbase.com/learn/crypto-basics/what-is-dollar-cost-averaging-dca",
    "https://www.coinbase.com/learn/crypto-basics/what-are-decentralized-autonomous-organizations",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-memecoin",
    "https://www.coinbase.com/learn/crypto-basics/proof-of-work-pow-vs-proof-of-stake-pos-what-is-the-difference",
    "https://www.coinbase.com/learn/crypto-basics/how-to-set-up-a-crypto-wallet",
    "https://www.coinbase.com/learn/crypto-tips/what-is-staking",
    "https://www.coinbase.com/learn/tips-and-tutorials/how-to-read-crypto-charts",
    "https://www.coinbase.com/learn/tips-and-tutorials/what-is-defi",
    "https://www.coinbase.com/learn/crypto-basics/what-are-nfts",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-smart-contract",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-gamefi",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-bitcoin-halving",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-dex",
    "https://www.coinbase.com/learn/crypto-basics/what-is-internet-computer",
    "https://www.coinbase.com/learn/crypto-basics/what-is-proof-of-work-or-proof-of-stake",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-protocol",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-private-key",
    "https://www.coinbase.com/learn/crypto-basics/what-are-technical-analysis-and-fundamental-analysis",
    "https://www.coinbase.com/learn/crypto-basics/what-is-volatility",
    "https://www.coinbase.com/learn/crypto-basics/what-is-uniswap",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-hash-rate",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-erc-721",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-the-ethereum-virtual-machine",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-a-node-in-cryptocurrency",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-sidechains",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-brc-20-tokens",
    "https://www.coinbase.com/learn/crypto-basics/what-is-cloud-mining-in-crypto",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-zero-knowledge-proofs",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-delegated-proof-of-stake-dpos",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-layer-0-protocols",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-socialfi",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-impermanent-loss",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-real-world-assets-rwa",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-nft-finance",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-sandwich-attacks-in-crypto",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-etherscan-and-how-to-use-it",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-a-blockchain-genesis-block",
    "https://www.coinbase.com/learn/crypto-glossary/what-are-bitcoin-layer-2-blockchains",
    "https://www.coinbase.com/learn#advanced-trading",
    "https://www.coinbase.com/learn/crypto-glossary/what-is-erc-20",
    "https://www.coinbase.com/learn/crypto-basics/what-is-the-difference-between-a-coin-and-a-token",
    "https://www.coinbase.com/learn/crypto-basics/what-is-a-token",
]

def scrape_single_article(url):
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(random.uniform(3, 5))
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        text = "\n".join([p.text for p in paragraphs if p.text.strip()])
        driver.quit()
        return {"url": url, "text": text}
    except Exception as e:
        print(f" Error scraping {url}: {e}")
        return {"url": url, "text": ""}

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # Load existing articles (if any)
    existing = []
    path = "data/coinbase_articles.json"
    if os.path.exists(path):
        with open(path) as f:
            existing = json.load(f)

    existing_urls = {item["url"] for item in existing}
    new_urls = [url for url in URLS if url not in existing_urls]

    print(f" {len(existing)} articles already scraped.")
    print(f" {len(new_urls)} new URLs to scrape...")

    new_articles = [scrape_single_article(url) for url in new_urls]
    merged = existing + new_articles

    with open(path, "w") as f:
        json.dump(merged, f, indent=2)

    print(f"Added {len(new_articles)} new articles. Total now: {len(merged)}")
os.system("python build_index.py")
