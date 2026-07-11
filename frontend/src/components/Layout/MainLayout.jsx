import { useEffect, useState } from "react";
import { Box, Grid, Paper } from "@mui/material";

import Navbar from "./Navbar";
import AIAssistant from "../AI/AIAssistant";
import InteractionForm from "../Interaction/InteractionForm";
import InteractionTable from "../Interaction/InteractionTable";

import {
  getInteractions,
  createInteraction,
  updateInteraction,
  deleteInteraction,
} from "../../services/api";

export default function MainLayout({
  interactionData,
  setInteractionData,
  refreshTable,
  setRefreshTable,
}) {
  const [interactions, setInteractions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [editingInteraction, setEditingInteraction] = useState(null);

  const fetchInteractions = async () => {
    try {
      setLoading(true);
      const data = await getInteractions();
      setInteractions(data);
    } catch (error) {
      console.error("Failed to fetch interactions:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchInteractions();
  }, [refreshTable]);

  const saveInteraction = async (data) => {
    try {
      if (editingInteraction) {
        await updateInteraction(editingInteraction.id, data);
        setEditingInteraction(null);
      } else {
        await createInteraction(data);
      }

      setInteractionData(null);
      setRefreshTable((prev) => !prev);
    } catch (error) {
      console.error("Save failed:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteInteraction(id);
      setRefreshTable((prev) => !prev);
    } catch (error) {
      console.error("Delete failed:", error);
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        bgcolor: "#f4f6f9",
      }}
    >
      <Navbar />

      <Box sx={{ p: 3 }}>
        <Grid container spacing={3}>

          {/* LEFT - Interaction Form */}

          <Grid size={{ xs: 12, md: 8 }}>
            <Paper
              elevation={3}
              sx={{
                height: 650,
                p: 3,
                borderRadius: 3,
                display: "flex",
                flexDirection: "column",
                overflow: "hidden",
              }}
            >
              <InteractionForm
                interactionData={interactionData}
                editingInteraction={editingInteraction}
                onSave={saveInteraction}
              />
            </Paper>
          </Grid>

          {/* RIGHT - AI Assistant */}

          <Grid size={{ xs: 12, md: 4 }}>
            <Paper
              elevation={3}
              sx={{
                height: 650,
                p: 2,
                borderRadius: 3,
                display: "flex",
                flexDirection: "column",
                overflow: "hidden",
              }}
            >
              <AIAssistant
                setInteractionData={setInteractionData}
              />
            </Paper>
          </Grid>

        </Grid>

        {/* Interaction History */}

        <Box mt={3}>
          <Paper
            elevation={3}
            sx={{
              p: 3,
              borderRadius: 3,
            }}
          >
            <InteractionTable
              interactions={interactions}
              loading={loading}
              onEdit={setEditingInteraction}
              onDelete={handleDelete}
            />
          </Paper>
        </Box>

      </Box>
    </Box>
  );
}