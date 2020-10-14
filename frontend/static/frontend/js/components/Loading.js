import React from "react";
import { MDBContainer as Container } from "mdbreact";

export default function Loading() {
  return (
    <Container className="text-center my-5 mt-5">
      <div className="my-5 mt-5 spinner-grow spinner-grow-lg text-primary d-inline-block" />
    </Container>
  );
}
