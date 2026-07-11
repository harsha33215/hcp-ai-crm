import { useState } from "react";
import MainLayout from "../components/Layout/MainLayout";

export default function Dashboard() {
  const [interactionData, setInteractionData] = useState(null);
  const [refreshTable, setRefreshTable] = useState(false);

  return (
    <MainLayout
      interactionData={interactionData}
      setInteractionData={setInteractionData}
      refreshTable={refreshTable}
      setRefreshTable={setRefreshTable}
    />
  );
}