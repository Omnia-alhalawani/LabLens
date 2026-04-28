import json
import urllib3
import base64
import os

http = urllib3.PoolManager()


def lambda_handler(event, context):
    # Load API key from Lambda environment variables (never hardcode secrets)
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

    try:
        # ================================
        # 1) Receive and decode the image
        # ================================
        body = event.get("body", "")

        # Handle base64-encoded body from API Gateway
        if event.get("isBase64Encoded", False):
            image_bytes = base64.b64decode(body)
        else:
            # Strip data URI prefix if present (e.g. data:image/jpeg;base64,...)
            if "base64," in body:
                body = body.split("base64,")[1]
            image_bytes = base64.b64decode(body)

        # Re-encode to a clean base64 string
        clean_b64 = base64.b64encode(image_bytes).decode("utf-8")

        # ================================
        # 2) Send image to Gemini API
        # ================================
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        )

        payload = {
            "contents": [{
                "parts": [
                    {
                        "text": (
                            "أنت LabLens. اقرأ التحاليل الطبية في الصورة "
                            "واشرحها بالعربي البسيط جداً مع 🟢 طبيعي و 🔴 غير طبيعي. "
                            "لا تقترح أدوية."
                        )
                    },
                    {
                        "inlineData": {
                            "mimeType": "image/jpeg",
                            "data": clean_b64
                        }
                    }
                ]
            }]
        }

        response = http.request(
            "POST",
            url,
            body=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        result = json.loads(response.data.decode("utf-8"))

        # ================================
        # 3) Return successful analysis
        # ================================
        if "candidates" in result:
            text = (
                result.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "No analysis returned")
            )

            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"analysis": text}, ensure_ascii=False)
            }

        # ================================
        # 4) Handle Gemini API failure
        # ================================
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(
                {"error": "Failed to analyze image. Please try again."},
                ensure_ascii=False
            )
        }

    except Exception as e:
        # ================================
        # 5) Handle unexpected errors
        # ================================
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({"error": str(e)}, ensure_ascii=False)
        }
