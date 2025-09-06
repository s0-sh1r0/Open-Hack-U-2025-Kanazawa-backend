import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from datetime import datetime

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_with_openai(request):
    reply = None
    user_message = None

    if request.method == "POST":
        # ユーザー入力を受け取る
        user_message = request.POST.get("message", "")

        if user_message:
            # OpenAI APIを呼ぶ
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたはソフトウェアの環境構築アシスタントです。可能な限り、回答はステップごとの手順としてまとめてください。"},
                    {"role": "user", "content": f"次のアプリの概要から環境構成を提案してください:\n\n{user_message}"},
                ],
            )

            # 応答を取り出し
            reply = response.choices[0].message.content

            # Markdownファイルに追記
            file_path = "output.md"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"## 質問 ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
                f.write(f"{user_message}\n\n")
                f.write("### 回答\n")
                f.write(f"{reply}\n\n---\n\n")

    return render(request, "chat.html", {"reply": reply, "user_message": user_message})
