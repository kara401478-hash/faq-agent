# 🤖 AI-FAQ 社内規定サポート窓口

社内規定（PDF）をAIが読み込み、自然な日本語で質問に答えてくれるチャットアプリです。

## 概要

「給与の支払日はいつ？」「賞与は何回？」など、社内規定に関する質問をAIが自動回答します。
PDFを差し替えるだけで、どんな会社の規定にも対応できます。

## 機能

- 社内規定PDFを自動読み込み
- 自然な日本語での質問に対応（「給料」→「賃金規定」も自動で解釈）
- 規定に記載がない場合は担当者への問い合わせを案内

## 技術スタック

| 技術 | 用途 |
|---|---|
| Python | メイン言語 |
| Streamlit | UI |
| Groq API (LLaMA 3.3) | LLM |
| pdfplumber | PDF読み込み |

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## セットアップ

1. `.streamlit/secrets.toml`を作成してGroq APIキーを設定

```toml
GROQ_API_KEY = "your_api_key_here"
```

2. `company_rules.pdf`を同じフォルダに配置

3. 起動！

## ポイント

規定のPDFを丸ごとLLMに渡すことで、キーワードの表記ゆれ（「給料」と「賃金」など）にも柔軟に対応しています。
