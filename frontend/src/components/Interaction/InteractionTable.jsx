import {
  Typography,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  IconButton,
  CircularProgress,
} from "@mui/material";

import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

export default function InteractionTable({
  interactions = [],
  loading,
  onEdit,
  onDelete,
}) {
  return (
    <>
      <Typography variant="h6" fontWeight={700} mb={2}>
        Interaction History
      </Typography>

      {loading ? (
        <CircularProgress />
      ) : (
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>HCP</TableCell>
              <TableCell>Hospital</TableCell>
              <TableCell>Meeting</TableCell>
              <TableCell>Summary</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            {interactions.length === 0 ? (
              <TableRow>
                <TableCell colSpan={6} align="center">
                  No Interactions Found
                </TableCell>
              </TableRow>
            ) : (
              interactions.map((item) => (
                <TableRow key={item.id}>
                  <TableCell>{item.id}</TableCell>

                  <TableCell>{item.hcp_name}</TableCell>

                  <TableCell>{item.hospital}</TableCell>

                  <TableCell>{item.meeting_type}</TableCell>

                  <TableCell>{item.summary}</TableCell>

                  <TableCell>
                    <IconButton onClick={() => onEdit(item)}>
                      <EditIcon />
                    </IconButton>

                    <IconButton color="error" onClick={() => onDelete(item.id)}>
                      <DeleteIcon />
                    </IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      )}
    </>
  );
}
