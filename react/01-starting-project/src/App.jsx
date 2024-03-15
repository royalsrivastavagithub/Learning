import { CORE_CONCEPTS } from "./data";
import Header from "./components/Header/Header";
import Core from "./components/Core";
import TabButton from "./components/TabButton";
import { useState } from "react";
import { EXAMPLES } from "./data";

console.log("APP Component Rendering");
function App() {
  const [selectedTopic, setSelectedTopic] = useState();

  function handleSelect(selectedButton) {
    console.log(selectedButton);
    setSelectedTopic(selectedButton);
  }

  return (
    <div>
      <Header></Header>
      <main>
        <section id="core-concepts">
          <h2>Learn New Stuff</h2>
          <ul>
          {CORE_CONCEPTS.map((conceptItem) => <Core key ={conceptItem.title}{...conceptItem}/>)}
          </ul>
        </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
            <TabButton isSelected={selectedTopic==='components'?true:undefined} onSelect={() => handleSelect("components")}>
              Components
            </TabButton>
            <TabButton isSelected={selectedTopic==='props'?true:undefined} onSelect={() => handleSelect("props")}>Props</TabButton>
            <TabButton isSelected={selectedTopic==='jsx'?true:undefined} onSelect={() => handleSelect("jsx")}>JSX</TabButton>
            <TabButton isSelected={selectedTopic==='state'?true:undefined}onSelect={() => handleSelect("state")}>State</TabButton>
          </menu>
          {!selectedTopic ? (
            <p>Please select a topic !</p>
          ) : (
            <div id="tab-content">
              <h3>{EXAMPLES[selectedTopic].title}</h3>
              <p>{EXAMPLES[selectedTopic].description}</p>
              <pre>
                <code>{EXAMPLES[selectedTopic].code}</code>
              </pre>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
