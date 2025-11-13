from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def example():
    browser = Browser(
        # use_cloud=True,  # クラウド版を使いたい場合はコメント解除
    )

    llm = ChatBrowserUse()

    agent = Agent(
        task="[重要]このタスクは3回のメッセージ送信が完了するまでdoneアクションを呼び出さないでください。手順：1. https://gemini.google.com/app?hl=ja にアクセスする。2. 1回目の送信：テキスト入力欄に「こんにちは」と入力し送信ボタンをクリックし、Geminiの返答が完全に表示されるまで待つ（最低5秒）。3. 2回目の送信：Geminiの返答内容を読み、その返答に対して適切な返信を考え（例：質問に答える、会話を続ける、感想を述べる）、考えた返信をテキスト入力欄に入力し送信ボタンをクリックし、再びGeminiの返答を待つ（最低5秒）。4. 3回目の送信：2回目のGeminiの返答内容を読み、その返答に対してさらに適切な返信を考え、考えた返信をテキスト入力欄に入力し送信ボタンをクリック。5. 完了条件の確認：あなたが3回メッセージを送信し、Geminiから少なくとも2回返答を受け取った場合のみdoneアクションを実行。注意：1回や2回の送信で終わらないこと、必ず3回送信するまで続けること、Geminiの返答内容に基づいて自然な会話を心がけること、各送信後は必ず返答を待つこと。",
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())
