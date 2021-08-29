import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Header from "../src/components/header/header"

import Home from "../src/pages/home"
import Categoria from "../src/pages/categoria"
import Favoritos from "../src/pages/favorito"
import PostPorId from "../src/pages/post-id"

const Routes = () =>{
    return(
        <BrowserRouter>
            <Header/>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/categoria/:cat" component={Categoria} />
                <Route exact path="/favoritos" component={Favoritos} />
                <Route exact path="/post/:id" component={PostPorId} />
                
            </Switch>
        </BrowserRouter>
    );
}

export default Routes;