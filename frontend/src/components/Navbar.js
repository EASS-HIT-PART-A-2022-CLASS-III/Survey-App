import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <h3>Survey App</h3>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/" className="nav-link">Question List</Link>
        </li>
        <li className="nav-item">
          <Link to="/add" className="nav-link">Add Question</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
