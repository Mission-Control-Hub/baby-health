import { Outlet, useNavigate, useLocation } from "react-router";
import { getIcon } from "../iconMap";
import { useUIBootstrap } from "../UIBootstrapContext";

export function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const { data, loading, error } = useUIBootstrap();

  const tabs = data?.content_shell?.tabs ?? [];

  return (
    <div className="max-w-md mx-auto min-h-screen bg-background relative" style={{ fontFamily: "'Inter', sans-serif" }}>
      <div className="pb-20 overflow-y-auto">
        {error && (
          <div className="mx-4 mt-4 rounded-2xl border border-destructive/30 bg-destructive/10 px-4 py-3 text-sm text-destructive">
            Não foi possível carregar os dados da API. Verifique o backend e VITE_API_BASE_URL.
          </div>
        )}
        {loading && !data && (
          <div className="px-5 pt-6 text-sm text-muted-foreground">Carregando…</div>
        )}
        <div className="px-5 pt-3 text-right"><button className="text-sm text-primary underline" onClick={() => navigate("/integrations")}>Integrações</button></div>
        <Outlet />
      </div>

      {/* Bottom Nav */}
      <nav className="fixed bottom-0 left-0 right-0 bg-card/95 backdrop-blur-md border-t border-border/50 z-40 max-w-md mx-auto">
        <div className="flex items-center justify-around py-2 px-2">
          {tabs.map((tab: { path: string; label: string; icon: string }) => {
            const isActive = location.pathname === tab.path;
            const TabIcon = getIcon(tab.icon);
            return (
              <button
                key={tab.path}
                onClick={() => navigate(tab.path)}
                className={`flex flex-col items-center gap-0.5 py-1 px-3 rounded-xl transition-colors ${
                  isActive ? "text-primary" : "text-muted-foreground"
                }`}
              >
                <TabIcon className={`w-6 h-6 ${isActive ? "fill-primary/20" : ""}`} />
                <span className="text-[10px]">{tab.label}</span>
              </button>
            );
          })}
        </div>
      </nav>
    </div>
  );
}
