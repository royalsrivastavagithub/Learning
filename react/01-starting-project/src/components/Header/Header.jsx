import headerImg from '../../assets/react-core-concepts.png'
import './Header.css'
const words = ["Fundamental", "Crucial", "Core", "All", "Every"];

function randInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

export default function Header() {
    const filler = words[randInt(4)];
  
    return (
      <header>
        <img src={headerImg} alt="Stylized atom" />
        <h1>React Essentials</h1>
        <p>
          {filler} React concepts you will need for almost any app you are going
          to build!
        </p>
      </header>
    );
  }