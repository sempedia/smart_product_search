## Run Locally

Clone the project

```bash
  git clone git@github.com:sempedia/smart_product_search.git
```

Go to the project directory

```bash
  cd ecommerce
```

Install dependencies

```bash
  npm install

  or

  npm install react-material-ui-carousel --save --legacy-peer-deps
```

Start the server

```bash
  npm start
```

The server should now be running. You can access the application by opening a web browser and entering the following URL:

```bash
  http://localhost:3000
```


# E-commerce AI Backend

This is the backend service for the E-commerce React application.
It provides an **AI-powered Smart Product Search** API that allows users to search for products using **natural language queries** such as:

> "Show me running shoes under $100 with good reviews"

---

## 🚀 How to Run the App

### 1️⃣ Navigate to the backend directory
```bash
cd api/smart_product_search
```

### 2️⃣ (Optional) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3️⃣ Install dependencies
```bash

pip install -r requirements.txt
```

### 4️⃣ Start the FastAPI server
```bash

uvicorn main:app --reload
```
### The backend will be running at:

```bash
http://localhost:8000
```

### You can view the interactive API docs here:

```bash
Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc
```


### 🤖 AI Feature
Chosen Feature:
Option A – Smart Product Search (NLP)

This feature allows users to:

Search using natural language instead of fixed keywords.

Apply filters like maximum price and rating from the query text.

Automatically match synonyms and variations (e.g., "men", "men's", "mens").

Example:

```bash

Query: "Show me running shoes under $100 with good reviews"
Result: List of products that are shoes, under $100, and have a high rating.
```

### 🛠 Tools & Libraries Used

- FastAPI → High-performance backend API framework.

- Uvicorn → ASGI server to run FastAPI.

- spaCy → Natural Language Processing (NLP) for extracting keywords, lemmas, and filtering.

- pydantic → Data validation and serialization.

- typing → Type hints for cleaner code.
Find them all in `api/smart_product_search/requirements.txt`

### 📦 Product Data Source

The product data used in this backend is **mocked** and fetched live from the public [FakeStoreAPI](https://fakestoreapi.com/), which provides fake e-commerce product data for testing and prototyping purposes.

This means:
- No real database is used.
- The product catalog is dynamic and reflects the current data from the FakeStoreAPI.
- Ideal for demo and development but not for production use.

---

### 📌 Assumptions

Only English language search queries are currently supported.

Price and rating filters are parsed directly from the user's query using regex + NLP.

Categories are optional — users can search across the entire catalog without selecting a category.

This backend is designed to integrate with the React frontend in the ecommerce root folder.

### 🧪 Testing the Smart Product Search API
```bash

Example request

GET http://localhost:8000/smart-product-search?query=shoes%20under%20$100

Example response:


[
  {
    "title": "Running Sneakers",
    "price": 89.99,
    "category": "Men's Shoes",
    "rating": 4.7
  }
]
```
### 📂 Project Structure
```bash
ecommerce/
├── api
│ ├── app.js
│ ├── config
│ │ ├── config.env.example
│ │ └── database.js
│ ├── controllers
│ │ ├── orderController.js
│ │ ├── paymentController.js
│ │ ├── productController.js
│ │ └── userController.js
│ ├── data
│ │ ├── cart.json
│ │ ├── images
│ │ │ ├── 1594728176097-61zBrD4EswL.AC_SL1500.jpg
│ │ │ └── ...
│ │ ├── invoice
│ │ │ ├── invoice-5f096ef911137b230cccbcde.pdf
│ │ │ └── ...
│ │ ├── products.json
│ │ └── util
│ │ ├── fileDelete.js
│ │ └── path.js
│ ├── middlewares
│ │ ├── common
│ │ ├── helpers
│ │ ├── user_actions
│ │ └── validator
│ ├── models
│ │ ├── Address.js
│ │ ├── Admin.js
│ │ ├── Product.js
│ │ └── ...
│ ├── public
│ │ ├── android-chrome-192x192.png
│ │ ├── css
│ │ └── js
│ ├── routes
│ │ ├── orderRoute.js
│ │ ├── paymentRoute.js
│ │ ├── productRoute.js
│ │ └── userRoute.js
│ ├── server.js
│ ├── smart_product_search***
│ │ ├── init.py
│ │ ├── main.py***
│ │ └── requirements.txt***
│ └── utils
│ ├── apiFeatures.js
│ └── ...
├── package.json
├── package-lock.json
├── public
│ ├── assets
│ ├── favicon.ico
│ ├── index.html
│ └── robots.txt
├── README.md
└── src
├── components
│ ├── Footer.jsx
│ ├── Navbar.jsx
│ ├── Products.jsx
│ ├── SmartProductSearch.jsx***
│ └── ...
├── index.js***
├── pages
│ ├── Home.jsx
│ ├── Product.jsx
│ ├── SmartProductSearchPage.jsx***
│ └── ...
└── redux
├── action
├── reducer
└── store.js
```

### Integration Explanation

- The **backend** FastAPI smart product search API is located inside `api/smart_product_search/`. This contains the AI-powered search logic and API endpoints.

- On the **frontend** React side, the AI feature is implemented via the `SmartProductSearch.jsx` component inside `src/components/`, and `SmartProductSearch.jsx` inside `src/pages` and routed through `eccommerce/src/index.jsx`.

- The frontend calls the backend API `api/smart_product_search/main.py`to fetch product search results dynamically based on user input, enabling an interactive AI-powered product search experience.

- The rest of the backend (`api/`) handles traditional e-commerce functionality like orders, payments, and user management, integrating seamlessly with the React frontend.

This structure allows you to develop and deploy the frontend React app and backend FastAPI AI functionality independently, yet they work together smoothly via API calls.

```