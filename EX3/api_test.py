from fastapi.testclient import TestClient
from main import app

client = TestClient(app) 

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, input your messege."}

def test_generate_text():
    item = {"text": "This is a test."}
    response = client.post("/generate/", json=item)
    assert response.status_code == 200
    results = response.json()
    assert isinstance(results, list)  # Проверяем, что ответ - это список
    assert len(results) > 0  # Проверяем, что список не пустой
    generated_text = results[0]["generated_text"]  # Обращаемся к первому элементу списка
    assert generated_text is not None

def test_generate_text_length():
    item = {"text": "This is a test."}
    response = client.post("/generate/", json=item)
    assert response.status_code == 200
    results = response.json()
    assert isinstance(results, list)  # Проверяем, что ответ - это список
    assert len(results) > 0  # Проверяем, что список не пустой
    generated_texts = [result["generated_text"][:20] for result in results]  # Получаем и обрезаем список сгенерированных текстов
    for generated_text in generated_texts:
        assert len(generated_text) <= 20, f"Generated text is longer than 20 characters: {generated_text}"



