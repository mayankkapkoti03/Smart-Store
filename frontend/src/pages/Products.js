import { useEffect, useState } from "react";
import API from "../api/axios";

function Products() {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");

  const fetchProducts = async () => {
    try {
      console.log("Searching:", search);

      const response = await API.get(`/products?search=${search}`);

      setProducts(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div>
      <input
        type="text"
        placeholder="Search products..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={fetchProducts}>Search</button>

      <br />
      <br />

      <h2>Products</h2>

      {products.length === 0 ? (
        <p>No products available</p>
      ) : (
        products.map((product) => (
          <div
            key={product.id || Math.random()}
            style={{
              border: "1px solid gray",
              padding: "10px",
              margin: "10px",
              width: "300px",
            }}
          >
            <h3>{product.name}</h3>
            <p>Price: ₹{product.price}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Products;
