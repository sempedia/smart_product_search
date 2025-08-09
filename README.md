# 🛒 E-commerce Platform with AI-Powered Smart Search

This project is an e-commerce platform with a **React** frontend and an **AI-powered backend** built with **FastAPI** and **spaCy** for natural language product search. The platform allows users to browse products and use an advanced search feature to find items using conversational queries.

---

### 💻 Frontend – E-commerce Website

This is a modern, React-based e-commerce website where users can:

* Browse a catalog of products (mocked using the Fake Store API).
* View detailed product information and categories.
* Interact with a clean, responsive UI built with Material UI and Carousel components.

#### How to Run the Frontend

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:sempedia/smart_product_search.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd ecommerce
    ```

3.  **Install dependencies:**
    ```bash
    npm install
    ```
    or
    ```bash
    npm install react-material-ui-carousel --save --legacy-peer-deps
    ```

4.  **Start the development server:**
    ```bash
    npm start
    ```
    The application will be accessible at: `http://localhost:3000`

---

### 🤖 Backend – E-commerce AI **NLP** Backend

This is the backend service for the E-commerce React application. It provides an **AI-powered Smart Product Search NLP API** that allows users to search for products using **natural language queries**, such as:

> "Show me running shoes under $100 with good reviews"

#### How to Run the Backend

1.  **Navigate to the backend directory:**
    ```bash
    cd api/smart_product_search
    ```

2.  **(Optional) Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The backend will be running at: `http://localhost:8000`

You can view the interactive API documentation here:
* **Swagger UI** → `http://localhost:8000/docs`
* **ReDoc** → `http://localhost:8000/redoc`

---

### 🧠 AI Feature Details

**Chosen Feature:** Option A – Smart Product Search (**NLP**)

This feature enables users to:
* Search using natural language instead of fixed keywords.
* Apply filters like maximum price and minimum rating directly from the query text.
* Automatically match synonyms and variations (e.g., "men", "men's", "mens").

**Example:**
* **Query:** "Show me running shoes under $100 with good reviews"
* **Result:** A list of products that are shoes, priced under $100, and have a high rating.

### 🛠 Tools & Libraries Used
The backend's AI functionality is powered by the following libraries:

* **FastAPI:** High-performance backend API framework.
* **Uvicorn:** ASGI server to run FastAPI.
* **spaCy:** A powerful Natural Language Processing (**NLP**) library for extracting keywords, lemmas, and applying filters from the query.
* **Pydantic:** Used for data validation and serialization.
* **Typing:** For type hints, ensuring cleaner and more maintainable code.

All dependencies can be found in `api/smart_product_search/requirements.txt`.

### 📦 Product Data Source

The product data is **mocked** and fetched live from the public **FakeStoreAPI**. This dynamic data source is ideal for development and testing purposes, meaning:

* No real database is used.
* The product catalog is always up-to-date with the FakeStoreAPI.
* This setup is perfect for demos but not intended for a production environment.

---

### 📌 Assumptions

* Only **English** language search queries are currently supported.
* Price and rating filters are parsed directly from the user's query using a combination of regex and **NLP**.
* Categories are optional; users can search across the entire catalog without specifying a category.
* The backend is designed to integrate with the React frontend in the `ecommerce` root folder.


### 🧪 Testing the Smart Product Search API

**Example request:**
```bash
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