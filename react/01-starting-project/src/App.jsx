import { CORE_CONCEPTS } from './data';
import Header from './components/Header/Header';
import Core from './components/Core';
import TabButton from './components/TabButton';

function App() {
  return (
    <div>
      <Header></Header>
      <main>
      <section id="core-concepts">
      <h2>Learn New Stuff</h2>
      <ul>
        <Core 
       {...CORE_CONCEPTS[3]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[2]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[1]}>  
        </Core>
        <Core 
       {...CORE_CONCEPTS[0]}>  
        </Core>
      </ul>
      </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
                <TabButton>Components</TabButton>
                <TabButton>Props</TabButton>
                <TabButton>JSX</TabButton>
                <TabButton>State</TabButton>
          </menu>
        </section>
      </main>
    </div>
  );
}

export default App;
