import { useEffect, useState } from "react";
import { authHeaders, buildApiUrl } from "@/api/client";

type KeyInfo = { id: string; name: string; grants: Record<string, string[]>; revoked: boolean; expires_at: string };
const modules: Record<string, string> = { feeding: "Alimentação", sleep: "Sono", hydration: "Hidratação", diapers: "Fraldas", activities: "Atividades", growth: "Crescimento", health: "Saúde", milestones: "Marcos", caregivers: "Cuidadores", profile: "Perfil", integrations: "Integrações" };
const actions: Record<string, string> = { read: "Consultar", write: "Criar e editar", delete: "Excluir", admin: "Administrar" };
async function request(path: string, init: RequestInit = {}) {
  const response = await fetch(buildApiUrl(path), { ...init, headers: { ...authHeaders(), "Content-Type": "application/json" } });
  if (!response.ok) throw new Error("Não foi possível concluir a operação. Verifique sua sessão e os dados informados.");
  return response.status === 204 ? null : response.json();
}
export function IntegrationsPage() {
  const [keys, setKeys] = useState<KeyInfo[]>([]);
  const [name, setName] = useState("");
  const [grants, setGrants] = useState<Record<string, string[]>>({});
  const [days, setDays] = useState(30);
  const [secret, setSecret] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const reload = async () => setKeys(await request("/api/integrations/keys"));
  useEffect(() => { reload().catch(e => setError(e.message)); }, []);
  async function create() {
    setBusy(true); setError(""); setSecret("");
    try {
      const result = await request("/api/integrations/keys", { method: "POST", body: JSON.stringify({ name, grants: Object.fromEntries(Object.entries(grants).filter(([,v]) => v.length)), expires_at: new Date(Date.now() + days * 86400000).toISOString() }) });
      setSecret(result.secret); setName(""); await reload();
    } catch (e) { setError((e as Error).message); } finally { setBusy(false); }
  }
  async function revoke(id: string) {
    setBusy(true); setError("");
    try { await request(`/api/integrations/keys/${id}`, { method: "DELETE" }); setSecret(""); await reload(); }
    catch (e) { setError((e as Error).message); } finally { setBusy(false); }
  }
  return <div className="p-5 space-y-5">
    <h1>Integrações</h1>
    <a className="text-primary underline" href={buildApiUrl("/docs")} target="_blank" rel="noreferrer">Abrir documentação da API (Swagger)</a>
    <p className="text-sm">Crie uma chave para conectar automações ao seu perfil. Apenas eventos dos trackers estão disponíveis nesta primeira versão. Permissões dos demais módulos serão usadas quando suas APIs forem disponibilizadas.</p>
    {error && <p role="alert">{error}</p>}
    {secret && <div className="p-4 bg-secondary rounded-2xl"><p>Copie sua chave agora. Ela será exibida apenas nesta criação.</p><code className="break-all select-all">{secret}</code><button className="block underline" onClick={() => setSecret("")}>Ocultar chave</button></div>}
    <label className="block">Nome da integração<input className="block border rounded p-2 w-full" value={name} maxLength={80} onChange={e => setName(e.target.value)} /></label>
    <label className="block">Validade<select value={days} onChange={e => setDays(Number(e.target.value))}><option value={7}>7 dias</option><option value={30}>30 dias</option><option value={90}>90 dias</option></select></label>
    <p className="text-sm">Sem seleção, o módulo fica sem acesso. Administrar inclui consultar, criar, editar e excluir naquele módulo.</p>
    {Object.entries(modules).map(([module, label]) => <fieldset key={module} className="border rounded-xl p-3"><legend>{label}</legend><div className="flex flex-wrap gap-3">{Object.entries(actions).map(([action, text]) => <label key={action} className="text-sm"><input type="checkbox" checked={(grants[module] ?? []).includes(action)} onChange={e => setGrants(old => ({ ...old, [module]: e.target.checked ? [...(old[module] ?? []), action] : (old[module] ?? []).filter(a => a !== action) }))} /> {text}</label>)}</div></fieldset>)}
    <button disabled={busy || !name.trim() || !Object.values(grants).some(a => a.length)} className="bg-primary text-primary-foreground rounded-xl p-3 disabled:opacity-50" onClick={create}>Criar API key</button>
    <h2>Suas chaves</h2>
    {!keys.length && <p>Nenhuma chave criada.</p>}
    {keys.map(key => <div key={key.id} className="border rounded-xl p-3"><p>{key.name} — {key.revoked ? "Revogada" : new Date(key.expires_at) <= new Date() ? "Expirada" : "Ativa"}</p><p className="text-xs">Expira em {new Date(key.expires_at).toLocaleString("pt-BR")}</p>{Object.entries(key.grants).map(([m,a]) => <p key={m} className="text-xs">{modules[m]}: {a.map(x => actions[x]).join(", ")}</p>)}{!key.revoked && <button disabled={busy} className="underline" onClick={() => revoke(key.id)}>Revogar chave</button>}</div>)}
  </div>;
}
