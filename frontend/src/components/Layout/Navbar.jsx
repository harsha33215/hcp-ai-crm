import { AppBar, Toolbar, Typography } from "@mui/material";

export default function Navbar() {
  return (
    <AppBar position="static" elevation={1}>
      <Toolbar>
        <Typography variant="h6" sx={{ fontWeight: 600 }}>
          HCP AI CRM
        </Typography>
      </Toolbar>
    </AppBar>
  );
}