import React, { Component } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import RoomJoinPage from "./RoomJoinPage";
import CreateRoomJoinPage from "./CreateRoomJoinPage";

class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<p>This is the home page</p>}></Route>
          <Route path="/join" element={<RoomJoinPage />} />
          <Route path="/create" element={<CreateRoomJoinPage />} />
        </Routes>
      </BrowserRouter>
    );
  }
}

export default HomePage;
