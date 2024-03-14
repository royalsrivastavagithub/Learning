import headerImg from './assets/react-core-concepts.png'
import { CORE_CONCEPTS } from './data';

const words = ["Fundamental", "Crucial", "Core", "All", "Every"];

function randInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

function Header() {
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

function Core({image, title,description}){
return(
  <li>
    <img src={image} alt={title} ></img>
    <h3>{title}</h3>
    <p>{description}</p>
  </li>

);
}

function App() {
  return (
    <div>
      <Header></Header>
      <main>
      <section id="core-concepts">
      <h2>Core Concepts</h2>
      <ul>
        <Core 
       {...CORE_CONCEPTS[0]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[1]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[2]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[3]}>  
        </Core>
      </ul>
      </section>
        
      </main>
    </div>
  );
}

export default App;
