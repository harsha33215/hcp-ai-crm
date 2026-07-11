import { useEffect, useState } from "react";

import {
  Box,
  Button,
  Grid,
  MenuItem,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

const initialForm = {
  hcp_name: "",
  hospital: "",
  meeting_type: "",
  discussion: "",
  summary: "",
  action_items: "",
};

export default function InteractionForm({
  onSave,
  editingInteraction,
  interactionData,
}) {
  const [form, setForm] = useState(initialForm);

  useEffect(() => {
    if (editingInteraction) {
      setForm({
        hcp_name: editingInteraction.hcp_name || "",
        hospital: editingInteraction.hospital || "",
        meeting_type: editingInteraction.meeting_type || "",
        discussion: editingInteraction.discussion || "",
        summary: editingInteraction.summary || "",
        action_items: editingInteraction.action_items || "",
      });
    }
  }, [editingInteraction]);

  useEffect(() => {
    if (interactionData) {
      setForm({
        hcp_name: interactionData.hcp_name || "",
        hospital: interactionData.hospital || "",
        meeting_type: interactionData.meeting_type || "",
        discussion: interactionData.discussion || "",
        summary: interactionData.summary || "",
        action_items: interactionData.action_items || "",
      });
    }
  }, [interactionData]);

  const handleChange = (e) => {
    setForm({
      ...form,

      [e.target.name]: e.target.value,
    });
  };

  const submit = async () => {
    if (!form.hcp_name.trim()) {
      alert("HCP Name required");
      return;
    }

    await onSave(form);

    setForm(initialForm);
  };

  return (
    <Box>
      <Typography variant="h5" fontWeight={700}>
        Interaction Form
      </Typography>

      <Typography color="text.secondary" mb={3}>
        Record healthcare professional interaction
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="HCP Name"
            name="hcp_name"
            value={form.hcp_name}
            onChange={handleChange}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Hospital"
            name="hospital"
            value={form.hospital}
            onChange={handleChange}
          />
        </Grid>

        <Grid item xs={12}>
          <TextField
            select
            fullWidth
            label="Meeting Type"
            name="meeting_type"
            value={form.meeting_type}
            onChange={handleChange}
          >
            <MenuItem value="Discussion">Discussion</MenuItem>

            <MenuItem value="Product Demo">Product Demo</MenuItem>

            <MenuItem value="Follow Up">Follow Up</MenuItem>
          </TextField>
        </Grid>

        <Grid item xs={12}>
          <TextField
            fullWidth
            multiline
            rows={6}
            label="Discussion"
            name="discussion"
            value={form.discussion}
            onChange={handleChange}
          />
        </Grid>

        <Grid item xs={12}>
          <TextField
            fullWidth
            multiline
            rows={3}
            label="Summary"
            name="summary"
            value={form.summary}
            onChange={handleChange}
          />
        </Grid>

        <Grid item xs={12}>
          <TextField
            fullWidth
            multiline
            rows={3}
            label="Action Items"
            name="action_items"
            value={form.action_items}
            onChange={handleChange}
          />
        </Grid>
      </Grid>

      <Stack direction="row" spacing={2} mt={3}>
        <Button variant="contained" onClick={submit}>
          {editingInteraction ? "Update" : "Save"}
        </Button>

        <Button variant="outlined" onClick={() => setForm(initialForm)}>
          Reset
        </Button>
      </Stack>
    </Box>
  );
}
