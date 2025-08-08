import React, { useState } from 'react';

const SmartProductSearch = () => {
  const [products, setProducts] = useState([]);
  const [recommended, setRecommended] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [maxPrice, setMaxPrice] = useState('');
  const [category, setCategory] = useState('');
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert('Please enter your search criteria.');
      return;
    }

    setLoading(true);
    setHasSearched(true);

    try {
      // Build query params dynamically
      const params = new URLSearchParams();
      params.append('query', searchTerm);
      if (maxPrice) params.append('maxPrice', maxPrice);
      if (category) params.append('category', category);

      // Use relative path so proxy works
      const response = await fetch(`/smart-product-search?${params.toString()}`);

      if (!response.ok) throw new Error('Failed to fetch products');
      const data = await response.json();

      setProducts(data.results);

      const recommendedProducts = [...data.results]
        .sort((a, b) => b.rating.rate - a.rating.rate)
        .slice(0, 5);

      setRecommended(recommendedProducts);
    } catch (error) {
      console.error(error);
      alert('Error fetching products');
      setProducts([]);
      setRecommended([]);
    }

    setLoading(false);
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: 900, margin: '0 auto', padding: 20 }}>
      <h1>Smart Product Search</h1>

      <div style={{ marginBottom: 20 }}>
        <input
          type="text"
          placeholder="Search products..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          style={{ padding: 8, width: 300, marginRight: 10 }}
        />
        <input
          type="number"
          placeholder="Max price"
          value={maxPrice}
          onChange={e => setMaxPrice(e.target.value)}
          style={{ padding: 8, width: 120, marginRight: 10 }}
        />
        <select
          value={category}
          onChange={e => setCategory(e.target.value)}
          style={{ padding: 8, marginRight: 10 }}
        >
          <option value="">All Categories</option>
          <option value="men's clothing">Men's Clothing</option>
          <option value="women's clothing">Women's Clothing</option>
          <option value="jewelery">Jewelery</option>
          <option value="electronics">Electronics</option>
        </select>
        <button onClick={handleSearch} style={{ padding: '8px 16px' }}>
          Search
        </button>
      </div>

      {loading && <p>Loading...</p>}

      {!loading && !hasSearched && (
        <p>Please enter your search criteria and click Search to see products.</p>
      )}

      {!loading && hasSearched && products.length === 0 && (
        <p>No products found matching your criteria.</p>
      )}

      {!loading && products.length > 0 && (
        <>
          <h2>Search Results ({products.length})</h2>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {products.map(product => (
              <li
                key={product.id}
                style={{
                  display: 'flex',
                  borderBottom: '1px solid #ccc',
                  padding: 10,
                  alignItems: 'center'
                }}
              >
                <img
                  src={product.image}
                  alt={product.title}
                  width={70}
                  height={70}
                  style={{ objectFit: 'contain', marginRight: 20 }}
                />
                <div style={{ flex: 1 }}>
                  <strong>{product.title}</strong>
                  <p style={{ margin: '5px 0' }}>${product.price.toFixed(2)}</p>
                  <p style={{ color: '#666' }}>{product.category}</p>
                </div>
                <div style={{ fontWeight: 'bold' }}>⭐ {product.rating.rate}</div>
              </li>
            ))}
          </ul>

          <h2>Recommended for You</h2>
          <ul
            style={{
              listStyle: 'none',
              padding: 0,
              display: 'flex',
              gap: 15,
              overflowX: 'auto'
            }}
          >
            {recommended.map(product => (
              <li
                key={product.id}
                style={{
                  border: '1px solid #ddd',
                  borderRadius: 8,
                  padding: 10,
                  width: 200,
                  flexShrink: 0
                }}
              >
                <img
                  src={product.image}
                  alt={product.title}
                  width="100%"
                  style={{ objectFit: 'contain', height: 150 }}
                />
                <h4 style={{ fontSize: 16 }}>{product.title}</h4>
                <p>${product.price.toFixed(2)}</p>
                <p style={{ fontSize: 12, color: '#555' }}>
                  Rating: {product.rating.rate} ({product.rating.count} reviews)
                </p>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default SmartProductSearch;
