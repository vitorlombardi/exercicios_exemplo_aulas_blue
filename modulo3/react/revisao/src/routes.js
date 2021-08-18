import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "./pages/home";
import Header from "./components/header"
import Filme from "./pages/filme"
import Favoritos from "./pages/favoritos"
import Erro from "./pages/erro"

const Routes = () => {
  return (
    <BrowserRouter>
    <Header/>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/filme/:id" component={Filme} />
        <Route exact path="/favoritos" component={Favoritos} />
        <Route  path="*" component={Erro} />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;